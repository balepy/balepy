from typing import Optional

from balepy.objects import HTTPMethod

import balepy


class GetUpdates:

    async def get_updates(
            self: "balepy.Client",
            offset: Optional[int] = -1,
            limit: Optional[int] = 100,
            timeout: Optional[int] = None,
            allowed_updates: Optional[list[str]] = None
    ) -> list:
        params: dict = {
            "offset": offset,
            "limit": limit,
        }
        if timeout is not None:
            params["timeout"] = timeout
        if allowed_updates is not None:
            params["allowed_updates"] = allowed_updates
        response_data = await self.api.execute(name="getUpdates", method=HTTPMethod.POST, data=params)
        return response_data["result"]
