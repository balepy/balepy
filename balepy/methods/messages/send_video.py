from typing import Optional, Union

from balepy.objects import HTTPMethod

import balepy


class SendVideo:

    async def send_video(
            self: 'balepy.Client',
            chat_id: Union[int, str],
            video: str,
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
            'video': video,
            'caption': caption,
            'parse_mode': parse_mode,
            'duration': duration,
            'width': width,
            'height': height,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup.to_dict() if hasattr(reply_markup, 'to_dict') else reply_markup
        }
        return await self.api.execute(name='sendVideo', method=HTTPMethod.POST, data=params)
