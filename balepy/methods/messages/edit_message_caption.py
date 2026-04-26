from typing import Optional, Union

from balepy.objects import HTTPMethod

import balepy


class EditMessageCaption:

    async def edit_message_caption(
            self: "balepy.Client",
            chat_id: Union[int, str],
            message_id: int,
            caption: Optional[str] = None,
            parse_mode: Optional[str] = None,
            reply_markup: Optional[dict] = None
    ) -> dict:
        params = {
            'chat_id': chat_id,
            'message_id': message_id,
            'caption': caption,
            'parse_mode': parse_mode,
            'reply_markup': reply_markup.to_dict() if hasattr(reply_markup, 'to_dict') else reply_markup
        }
        return await self.api.execute(name='editMessageCaption', method=HTTPMethod.POST, data=params)
