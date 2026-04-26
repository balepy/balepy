from typing import Optional

from balepy.objects import HTTPMethod

import balepy


class AnswerPreCheckoutQuery:

    async def answer_pre_checkout_query(
            self: "balepy.Client",
            pre_checkout_query_id: str,
            ok: bool = True,
            error_message: Optional[str] = None
    ) -> dict:
        params = {
            'pre_checkout_query_id': pre_checkout_query_id,
            'ok': ok,
        }
        if error_message is not None:
            params['error_message'] = error_message
        return await self.api.execute(name="answerPreCheckoutQuery", method=HTTPMethod.POST, data=params)
