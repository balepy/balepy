from typing import Optional, Union

from balepy.objects import HTTPMethod

import balepy


class SendAudio:

    async def send_audio(
            self: 'balepy.Client',
            chat_id: Union[int, str],
            audio: str,
            caption: Optional[str] = None,
            parse_mode: Optional[str] = None,
            duration: Optional[int] = None,
            performer: Optional[str] = None,
            title: Optional[str] = None,
            reply_to_message_id: Optional[int] = None,
            reply_markup: Optional[dict] = None
    ) -> dict:
        params = {
            'chat_id': chat_id,
            'audio': audio,
            'caption': caption,
            'parse_mode': parse_mode,
            'duration': duration,
            'performer': performer,
            'title': title,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup.to_dict() if hasattr(reply_markup, 'to_dict') else reply_markup
        }
        return await self.api.execute(name="sendAudio", method=HTTPMethod.POST, data=params)
