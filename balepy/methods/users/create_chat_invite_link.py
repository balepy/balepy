from typing import Optional, Union
from balepy.objects import HTTPMethod
from balepy.types import InviteLink
import balepy

class CreateChatInviteLink:
    async def create_chat_invite_link(
            self: "balepy.Client",
            chat_id: Union[int, str],
            name: Optional[str] = None,
            expire_date: Optional[int] = None,
            member_limit: Optional[int] = None,
            creates_join_request: Optional[bool] = None
    ) -> InviteLink:
        params = {
            'chat_id': chat_id,
            'name': name,
            'expire_date': expire_date,
            'member_limit': member_limit,
            'creates_join_request': creates_join_request
        }
        response = await self.api.execute(name="createChatInviteLink", method=HTTPMethod.POST, data=params)
        return InviteLink(response)
