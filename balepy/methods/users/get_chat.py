from typing import Union
from balepy.objects import HTTPMethod
from balepy.types import ChatFullInfo
import balepy

class GetChat:
    async def get_chat(self: "balepy.Client", chat_id: Union[int, str]) -> ChatFullInfo:
        params = {'chat_id': chat_id}
        response = await self.api.execute(name="getChat", method=HTTPMethod.POST, data=params)
        return ChatFullInfo(response)
