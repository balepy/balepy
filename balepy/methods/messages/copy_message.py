from typing import Optional, Union

from balepy.objects import HTTPMethod

import balepy


class CopyMessage:

    async def copy_message(
            self: "balepy.Client",
            chat_id: Union[int, str],
            from_chat_id: Union[int, str],
            message_id: int,
            caption: Optional[str] = None,
            reply_to_message_id: Optional[int] = None,
            reply_markup: Optional[dict] = None
    ) -> dict:
        params = {
            'chat_id': chat_id,
            'from_chat_id': from_chat_id,
            'message_id': message_id,
            'caption': caption,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup.to_dict() if hasattr(reply_markup, 'to_dict') else reply_markup
        }
        return await self.api.execute(name="copyMessage", method=HTTPMethod.POST, data=params)
