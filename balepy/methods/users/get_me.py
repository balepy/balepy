from balepy.objects import HTTPMethod
from balepy.types import User

import balepy


class GetMe:

    async def get_me(self: "balepy.Client") -> User:
        response = await self.api.execute(name="getMe", method=HTTPMethod.GET)
        return User(response)
