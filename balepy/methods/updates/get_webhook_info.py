from balepy.objects import HTTPMethod
from balepy.types import WebHookInfo

import balepy


class GetWebhookInfo:

    async def get_webhook_info(
            self: "balepy.Client"
    ) -> WebHookInfo:
        response = await self.api.execute(name="getWebhookInfo", method=HTTPMethod.POST)
        return WebHookInfo(response)
