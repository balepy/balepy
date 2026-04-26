from typing import Union
from balepy.objects import HTTPMethod
import balepy

class SetChatDescription:
    async def set_chat_description(self: "balepy.Client", chat_id: Union[int, str], description: str) -> dict:
        params = {'chat_id': chat_id, 'description': description}
        return await self.api.execute(name="setChatDescription", method=HTTPMethod.POST, data=params)
