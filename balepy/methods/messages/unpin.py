from typing import Union

from balepy.objects import HTTPMethod

import balepy


class UnpinChatMessage:

    async def unpin(
            self: "balepy.Client",
            chat_id: Union[int, str],
            message_id: int
    ) -> dict:
        params = {
            'chat_id': chat_id,
            'message_id': message_id,
        }
        return await self.api.execute(name="unpinChatMessage", method=HTTPMethod.POST, data=params)
