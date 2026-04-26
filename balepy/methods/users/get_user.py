from typing import Union
from balepy.objects import HTTPMethod
from balepy.types import ChatFullInfo
import balepy


class GetUser:

    async def get_user(self: "balepy.Client", user_id: Union[int, str]) -> ChatFullInfo:
        params = {'chat_id': user_id}
        response = await self.api.execute(name="getChat", method=HTTPMethod.POST, data=params)
        return ChatFullInfo(response)
