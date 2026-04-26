from typing import Union
from balepy.objects import HTTPMethod
from balepy.types import InviteLink
import balepy

class RevokeChatInviteLink:
    async def revoke_chat_invite_link(self: "balepy.Client", chat_id: Union[int, str], invite_link: str) -> InviteLink:
        params = {'chat_id': chat_id, 'invite_link': invite_link}
        response = await self.api.execute(name="revokeChatInviteLink", method=HTTPMethod.POST, data=params)
        return InviteLink(response)
