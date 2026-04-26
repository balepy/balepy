from typing import Optional, Union

from balepy.objects import HTTPMethod

import balepy


class EditMessageReplyMarkup:

    async def edit_message_reply_markup(
            self: "balepy.Client",
            chat_id: Union[int, str],
            message_id: int,
            reply_markup: Optional[dict] = None
    ) -> dict:
        params = {
            'chat_id': chat_id,
            'message_id': message_id,
            'reply_markup': reply_markup.to_dict() if hasattr(reply_markup, 'to_dict') else reply_markup
        }
        return await self.api.execute(name='editMessageReplyMarkup', method=HTTPMethod.POST, data=params)
