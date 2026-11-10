import os
import json
import mimetypes

from pathlib import Path
from typing import Optional

import aiohttp

from balepy.types import Results
from balepy.errors import APIError


class API:

    BASE_URL = "https://tapi.bale.ai"

    def __init__(self, client=None):
        self.client = client

    @staticmethod
    def _is_file(value):
        """Check whether a value represents an uploadable file."""

        if isinstance(value, (bytes, bytearray, memoryview)):
            return True

        if isinstance(value, os.PathLike):
            return True

        if isinstance(value, str) and os.path.isfile(value):
            return True

        if hasattr(value, "read") and callable(value.read):
            return True

        return False

    @staticmethod
    def _add_form_field(form, key, value, opened_files):
        """Add a value to multipart form data."""

        filename = None
        content_type = None

        if isinstance(value, (str, os.PathLike)) and os.path.isfile(value):
            file_path = Path(value)
            file_obj = open(file_path, "rb")
            opened_files.append(file_obj)

            filename = file_path.name
            content_type = (
                mimetypes.guess_type(filename)[0]
                or "application/octet-stream"
            )

            form.add_field(
                key,
                file_obj,
                filename=filename,
                content_type=content_type
            )

        elif isinstance(value, os.PathLike):
            raise FileNotFoundError(str(value))

        elif isinstance(value, (bytes, bytearray, memoryview)):
            filename = f"{key}.bin"

            form.add_field(
                key,
                bytes(value),
                filename=filename,
                content_type="application/octet-stream"
            )

        elif hasattr(value, "read") and callable(value.read):
            filename = getattr(value, "name", None)

            if filename:
                filename = os.path.basename(str(filename))
            else:
                filename = f"{key}.bin"

            content_type = (
                mimetypes.guess_type(filename)[0]
                or "application/octet-stream"
            )

            form.add_field(
                key,
                value,
                filename=filename,
                content_type=content_type
            )

        elif isinstance(value, (dict, list, tuple)):
            form.add_field(key, json.dumps(value, ensure_ascii=False))

        elif isinstance(value, bool):
            form.add_field(key, json.dumps(value))

        else:
            form.add_field(key, str(value))

    async def execute(
        self,
        name: str,
        method: Optional[str] = "GET",
        data: Optional[dict] = None
    ):
        """
        Execute asynchronous request to Bale API.

        Supports:
        - JSON requests
        - Multipart file uploads
        - bytes
        - Local file paths
        - pathlib.Path
        - Open file objects
        """

        base_url = self.client.base_url or self.BASE_URL
        path = f"/bot{self.client.bot_token}/{name}"

        timeout = aiohttp.ClientTimeout(
            total=self.client.timeout
        )

        if data is not None:
            data = {
                k: v for k, v in data.items()
                if v is not None
            }

        # Detect whether the request contains an uploadable file.
        has_files = (
            data is not None
            and any(self._is_file(v) for v in data.values())
        )

        for _ in range(self.client.max_retry):

            opened_files = []

            try:
                async with aiohttp.ClientSession(
                    base_url=base_url,
                    timeout=timeout
                ) as session:

                    if has_files:
                        form = aiohttp.FormData()

                        for key, value in data.items():
                            self._add_form_field(
                                form,
                                key,
                                value,
                                opened_files
                            )

                        request_kwargs = {"data": form}

                    else:
                        request_kwargs = {"json": data}

                    async with session.request(
                        method=method,
                        url=path,
                        **request_kwargs
                    ) as response:

                        response_data = await response.json()

                        if response_data.get("ok"):
                            response_data.pop("ok")
                            return response_data

                        error_code = response_data.get("error_code")
                        description = response_data.get("description")

                        raise APIError(description, error_code)

            finally:
                for file_obj in opened_files:
                    file_obj.close()

