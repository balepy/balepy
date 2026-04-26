from typing import Union

from balepy.objects import HTTPMethod

import balepy


class PinChatMessage:

    async def pin(
            self: "balepy.Client",
            chat_id: Union[int, str],
            message_id: int,
            disable_notification: bool = False
    ) -> dict:
        params = {
            'chat_id': chat_id,
            'message_id': message_id,
            'disable_notification': disable_notification,
        }
        return await self.api.execute(name="pinChatMessage", method=HTTPMethod.POST, data=params)
