from typing import Optional, Union

from balepy.objects import HTTPMethod

import balepy


class SendLocation:

    async def send_location(
            self: "balepy.Client",
            chat_id: Union[int, str],
            latitude: float,
            longitude: float,
            horizontal_accuracy: Optional[float] = None,
            reply_to_message_id: Optional[int] = None,
            reply_markup: Optional[dict] = None
    ) -> dict:
        params = {
            'chat_id': chat_id,
            'latitude': latitude,
            'longitude': longitude,
            'horizontal_accuracy': horizontal_accuracy,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup.to_dict() if hasattr(reply_markup, 'to_dict') else reply_markup
        }
        return await self.api.execute(name="sendLocation", method=HTTPMethod.POST, data=params)
