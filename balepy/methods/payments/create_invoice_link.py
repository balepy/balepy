import json
from balepy.objects import HTTPMethod
from balepy.types import LabeledPrice

import balepy


class CreateInvoiceLink:

    async def create_invoice_link(
            self: "balepy.Client",
            title: str,
            description: str,
            payload: str,
            prices: list
    ) -> dict:
        serialized_prices = [
            p.to_dict() if hasattr(p, "to_dict") else p
            for p in prices
        ]
        params = {
            "title": title,
            "description": description,
            "payload": payload,
            "provider_token": self.wallet_token,
            "prices": json.dumps(serialized_prices, ensure_ascii=False),
        }
        return await self.api.execute(name="createInvoiceLink", method=HTTPMethod.POST, data=params)
