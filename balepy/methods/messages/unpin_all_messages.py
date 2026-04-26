from typing import Union

from balepy.objects import HTTPMethod

import balepy


class UnpinAllChatMessages:

    async def unpin_all_messages(
            self: "balepy.Client",
            chat_id: Union[int, str]
    ) -> dict:
        params = {
            'chat_id': chat_id
        }
        return await self.api.execute(name="unpinAllChatMessages", method=HTTPMethod.POST, data=params)
