from typing import Optional, Union

from balepy.objects import HTTPMethod

import balepy


class SendMediaGroup:

    async def send_media_group(
            self: "balepy.Client",
            chat_id: Union[int, str],
            media: list[dict],
            reply_to_message_id: Optional[int] = None
    ) -> dict:
        params = {
            'chat_id': chat_id,
            'media': media,
            'reply_to_message_id': reply_to_message_id
        }
        return await self.api.execute(name="sendMediaGroup", method=HTTPMethod.POST, data=params)
