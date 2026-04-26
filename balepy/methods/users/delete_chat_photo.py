from typing import Union
from balepy.objects import HTTPMethod
import balepy

class DeleteChatPhoto:
    async def delete_chat_photo(self: "balepy.Client", chat_id: Union[int, str]) -> dict:
        params = {'chat_id': chat_id}
        return await self.api.execute(name="deleteChatPhoto", method=HTTPMethod.POST, data=params)
