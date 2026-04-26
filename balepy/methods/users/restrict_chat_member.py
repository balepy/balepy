from typing import Optional, Union
from balepy.objects import HTTPMethod
from balepy.types import ChatPermissions
import balepy


class RestrictChatMember:

    async def restrict_chat_member(
            self: "balepy.Client",
            chat_id: Union[int, str],
            user_id: int,
            permissions: ChatPermissions,
            until_date: Optional[int] = None
    ) -> dict:
        params = {
            "chat_id": chat_id,
            "user_id": user_id,
            "permissions": permissions.to_dict() if hasattr(permissions, "to_dict") else permissions,
            "until_date": until_date,
        }
        return await self.api.execute(name="restrictChatMember", method=HTTPMethod.POST, data=params)
