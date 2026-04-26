from typing import Optional, Union

from balepy.objects import HTTPMethod

import balepy


class BanChatMember:

    async def ban_chat_member(
            self: "balepy.Client",
            chat_id: Union[int, str],
            user_id: int,
            until_date: Optional[int] = None,
            revoke_messages: Optional[bool] = None
    ) -> dict:
        params = {
            'chat_id': chat_id,
            'user_id': user_id,
            'until_date': until_date,
            'revoke_messages': revoke_messages
        }
        return await self.api.execute(name="banChatMember", method=HTTPMethod.POST, data=params)
