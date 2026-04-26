from balepy.objects import HTTPMethod
import balepy

class DeleteMyCommands:
    async def delete_my_commands(self: "balepy.Client") -> dict:
        return await self.api.execute(name="deleteMyCommands", method=HTTPMethod.POST)
