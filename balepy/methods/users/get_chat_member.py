from typing import Union
from balepy.objects import HTTPMethod
from balepy.types import ChatMember
import balepy

class GetChatMember:
    async def get_chat_member(self: "balepy.Client", chat_id: Union[int, str], user_id: int) -> ChatMember:
        params = {'chat_id': chat_id, 'user_id': user_id}
        response = await self.api.execute(name="getChatMember", method=HTTPMethod.POST, data=params)
        return ChatMember(response)
