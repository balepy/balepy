from typing import Optional

from balepy.objects import HTTPMethod

import balepy


class AnwserCallbackQuery:

    async def anwser_callback_query(
            self: "balepy.Client",
            callback_query_id: str,
            text: Optional[str] = None,
            show_alert: bool = False,
            url: Optional[str] = None,
            cache_time: Optional[int] = None
    ) -> dict:
        params = {
            'callback_query_id': callback_query_id,
            'text': text,
            'show_alert': show_alert,
            'url': url,
            'cache_time': cache_time
        }
        return await self.api.execute(name="answerCallbackQuery", method=HTTPMethod.POST, data=params)
