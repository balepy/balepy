from balepy.objects import HTTPMethod

import balepy


class LogOut:

    async def log_out(self: 'balepy.Client') -> dict:
        return await self.api.execute(name="logout", method=HTTPMethod.GET)
