from balepy.objects import HTTPMethod
from balepy.types import File

import balepy


class GetFile:

    async def get_file(
            self: "balepy.Client",
            file_id: str
    ) -> File:
        params = {
            'file_id': file_id
        }
        response = await self.api.execute(name="getFile", method=HTTPMethod.POST, data=params)
        return File(response)

    def get_file_url(self, file_path: str) -> str:
        base_url = self.base_url or "https://tapi.bale.ai"
        return f"{base_url}/file/bot{self.bot_token}/{file_path}"
