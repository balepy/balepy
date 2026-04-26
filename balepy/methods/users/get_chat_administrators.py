from typing import Union
from balepy.objects import HTTPMethod
from balepy.types import ChatMember
import balepy

class GetChatAdministrators:
    async def get_chat_administrators(self: "balepy.Client", chat_id: Union[int, str]) -> list[ChatMember]:
        params = {'chat_id': chat_id}
        response = await self.api.execute(name="getChatAdministrators", method=HTTPMethod.POST, data=params)
        result = response.get("result", [])
        return [ChatMember(m) for m in result]
