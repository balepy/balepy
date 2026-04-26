from typing import Union

from balepy.objects import HTTPMethod

import balepy


class ForwardMessage:

    async def forward_message(
            self: "balepy.Client",
            chat_id: Union[int, str],
            from_chat_id: Union[int, str],
            message_id: int
    ) -> dict:
        params = {
            'chat_id': chat_id,
            'from_chat_id': from_chat_id,
            'message_id': message_id
        }
        return await self.api.execute(name="forwardMessage", method=HTTPMethod.POST, data=params)
