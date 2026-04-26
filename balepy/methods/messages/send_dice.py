from typing import Optional, Union

from balepy.objects import HTTPMethod

import balepy


class SendDice:

    async def send_dice(
            self: "balepy.Client",
            chat_id: Union[int, str],
            emoji: Optional[str] = None,
            reply_to_message_id: Optional[int] = None,
            reply_markup: Optional[dict] = None
    ) -> dict:
        params = {
            'chat_id': chat_id,
            'emoji': emoji,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup.to_dict() if hasattr(reply_markup, 'to_dict') else reply_markup
        }
        return await self.api.execute(name="sendDice", method=HTTPMethod.POST, data=params)
