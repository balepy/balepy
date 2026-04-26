from typing import Optional, Union
import json

from balepy.objects import HTTPMethod
from balepy.types import LabeledPrice

import balepy


class SendInvoice:

    async def send_invoice(
            self: "balepy.Client",
            chat_id: Union[int, str],
            title: str,
            description: str,
            payload: str,
            prices: list,
            photo_url: Optional[str] = None,
            photo_size: Optional[int] = None,
            photo_width: Optional[int] = None,
            photo_height: Optional[int] = None,
            need_name: Optional[bool] = None,
            need_phone_number: Optional[bool] = None,
            need_email: Optional[bool] = None,
            is_flexible: Optional[bool] = None,
            reply_to_message_id: Optional[int] = None,
            reply_markup=None
    ) -> dict:
        serialized_prices = [
            p.to_dict() if hasattr(p, "to_dict") else p
            for p in prices
        ]
        markup_dict = reply_markup.to_dict() if hasattr(reply_markup, "to_dict") else reply_markup
        params = {
            "chat_id": chat_id,
            "title": title,
            "description": description,
            "payload": payload,
            "provider_token": self.wallet_token,
            "prices": json.dumps(serialized_prices, ensure_ascii=False),
            "photo_url": photo_url,
            "photo_size": photo_size,
            "photo_width": photo_width,
            "photo_height": photo_height,
            "need_name": need_name,
            "need_phone_number": need_phone_number,
            "need_email": need_email,
            "is_flexible": is_flexible,
            "reply_to_message_id": reply_to_message_id,
            "reply_markup": markup_dict,
        }
        return await self.api.execute(name="sendInvoice", method=HTTPMethod.POST, data=params)
