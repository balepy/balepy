from typing import Optional, Union

from balepy.objects import HTTPMethod

import balepy


class EditMessageText:

    async def edit_message_text(
            self: "balepy.Client",
            text: str,
            chat_id: Optional[Union[int, str]] = None,
            message_id: Optional[int] = None,
            parse_mode: Optional[str] = None,
            reply_markup: Optional[dict] = None
    ) -> dict:
        params = {
            'chat_id': chat_id,
            'message_id': message_id,
            'text': text,
            'parse_mode': parse_mode,
            'reply_markup': reply_markup.to_dict() if hasattr(reply_markup, 'to_dict') else reply_markup
        }
        return await self.api.execute(name='editMessageText', method=HTTPMethod.POST, data=params)
