from typing import Optional, Union

from balepy.objects import HTTPMethod

import balepy


class SendDocument:

    async def send_document(
            self: 'balepy.Client',
            chat_id: Union[int, str],
            document: str,
            caption: Optional[str] = None,
            parse_mode: Optional[str] = None,
            reply_to_message_id: Optional[int] = None,
            reply_markup: Optional[dict] = None
    ) -> dict:
        params = {
            'chat_id': chat_id,
            'document': document,
            'caption': caption,
            'parse_mode': parse_mode,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup.to_dict() if hasattr(reply_markup, 'to_dict') else reply_markup
        }
        return await self.api.execute(name="sendDocument", method=HTTPMethod.POST, data=params)
