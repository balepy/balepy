from typing import Union
from balepy.objects import HTTPMethod
import balepy

class LeaveChat:
    async def leave_chat(self: "balepy.Client", chat_id: Union[int, str]) -> dict:
        params = {'chat_id': chat_id}
        return await self.api.execute(name="leaveChat", method=HTTPMethod.POST, data=params)
