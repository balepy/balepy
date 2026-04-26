from typing import Union

from balepy.objects import HTTPMethod

import balepy


class SendChatAction:

    async def send_chat_action(
            self: "balepy.Client",
            chat_id: Union[int, str],
            action: str
    ) -> dict:
        params = {
            'chat_id': chat_id,
            'action': action
        }
        return await self.api.execute(name="sendChatAction", method=HTTPMethod.POST, data=params)
