from typing import Union
from balepy.objects import HTTPMethod
import balepy


class SetChatAdministratorCustomTitle:

    async def set_chat_administrator_custom_title(
            self: "balepy.Client",
            chat_id: Union[int, str],
            user_id: int,
            custom_title: str
    ) -> dict:
        params = {
            'chat_id': chat_id,
            'user_id': user_id,
            'custom_title': custom_title
        }
        return await self.api.execute(name="setChatAdministratorCustomTitle", method=HTTPMethod.POST, data=params)
