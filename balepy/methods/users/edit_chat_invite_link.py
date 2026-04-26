from typing import Optional, Union
from balepy.objects import HTTPMethod
from balepy.types import InviteLink
import balepy


class EditChatInviteLink:

    async def edit_chat_invite_link(
            self: "balepy.Client",
            chat_id: Union[int, str],
            invite_link: str,
            name: Optional[str] = None,
            expire_date: Optional[int] = None,
            member_limit: Optional[int] = None,
            creates_join_request: Optional[bool] = None
    ) -> InviteLink:
        params = {
            'chat_id': chat_id,
            'invite_link': invite_link,
            'name': name,
            'expire_date': expire_date,
            'member_limit': member_limit,
            'creates_join_request': creates_join_request
        }
        response = await self.api.execute(name="editChatInviteLink", method=HTTPMethod.POST, data=params)
        return InviteLink(response)
