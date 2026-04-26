from typing import Optional

from balepy.objects import HTTPMethod

import balepy


class SetWebhook:

    async def set_webhook(
            self: "balepy.Client",
            url: str,
            max_connections: Optional[int] = None,
            allowed_updates: Optional[list[str]] = None
    ) -> dict:
        params = {
            'url': url,
            'max_connections': max_connections,
            'allowed_updates': allowed_updates
        }
        return await self.api.execute(name="setWebhook", method=HTTPMethod.POST, data=params)
