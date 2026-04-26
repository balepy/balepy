from typing import Union

from balepy.objects import HTTPMethod

import balepy


class UnbanChatMember:

    async def unban_chat_member(
            self: "balepy.Client",
            chat_id: Union[int, str],
            user_id: int,
            only_if_banned: bool = True
    ) -> dict:
        params = {
            'chat_id': chat_id,
            'user_id': user_id,
            'only_if_banned': only_if_banned,
        }
        return await self.api.execute(name="unbanChatMember", method=HTTPMethod.POST, data=params)
