from typing import Optional, Union

from balepy.objects import HTTPMethod

import balepy


class SendAnimation:

    async def send_animation(
            self: "balepy.Client",
            chat_id: Union[int, str],
            animation: str,
            caption: Optional[str] = None,
            parse_mode: Optional[str] = None,
            duration: Optional[int] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            reply_to_message_id: Optional[int] = None,
            reply_markup: Optional[dict] = None
    ) -> dict:
        params = {
            'chat_id': chat_id,
            'animation': animation,
            'caption': caption,
            'parse_mode': parse_mode,
            'duration': duration,
            'width': width,
            'height': height,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup.to_dict() if hasattr(reply_markup, 'to_dict') else reply_markup
        }
        return await self.api.execute(name='sendAnimation', method=HTTPMethod.POST, data=params)
