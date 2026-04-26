from typing import Union
from balepy.objects import HTTPMethod
import balepy


class InviteToChat:

    async def invite_to_chat(
            self: "balepy.Client",
            chat_id: Union[int, str],
            user_id: int
    ) -> dict:
        params = {'chat_id': chat_id, 'user_id': user_id}
        return await self.api.execute(name="inviteToChat", method=HTTPMethod.POST, data=params)
