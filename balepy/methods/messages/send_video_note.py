from typing import Optional, Union

from balepy.objects import HTTPMethod

import balepy


class SendVideoNote:

    async def send_video_note(
            self: "balepy.Client",
            chat_id: Union[int, str],
            video_note: str,
            duration: Optional[int] = None,
            length: Optional[int] = None,
            reply_to_message_id: Optional[int] = None,
            reply_markup: Optional[dict] = None
    ) -> dict:
        params = {
            'chat_id': chat_id,
            'video_note': video_note,
            'duration': duration,
            'length': length,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup.to_dict() if hasattr(reply_markup, 'to_dict') else reply_markup
        }
        return await self.api.execute(name="sendVideoNote", method=HTTPMethod.POST, data=params)
