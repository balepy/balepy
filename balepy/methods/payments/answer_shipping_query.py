from typing import Optional

from balepy.objects import HTTPMethod

import balepy


class AnswerShippingQuery:

    async def answer_shipping_query(
            self: "balepy.Client",
            shipping_query_id: str,
            ok: bool = True,
            shipping_options: Optional[list[dict]] = None,
            error_message: Optional[str] = None
    ) -> dict:
        params = {
            'shipping_query_id': shipping_query_id,
            'ok': ok,
        }
        if shipping_options is not None:
            params['shipping_options'] = shipping_options
        if error_message is not None:
            params['error_message'] = error_message
        return await self.api.execute(name="answerShippingQuery", method=HTTPMethod.POST, data=params)
