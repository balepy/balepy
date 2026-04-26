from balepy.objects import HTTPMethod

import balepy


class DeleteWebhook:

    async def delete_webhook(
            self: "balepy.Client"
    ) -> dict:
        return await self.api.execute(name="deleteWebhook", method=HTTPMethod.POST)
