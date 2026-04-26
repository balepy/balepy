from balepy.objects import HTTPMethod
from balepy.types import BotCommand
import balepy

class GetMyCommands:
    async def get_my_commands(self: "balepy.Client") -> list[BotCommand]:
        response = await self.api.execute(name="getMyCommands", method=HTTPMethod.GET)
        result = response.get("result", [])
        return [BotCommand(c["command"], c["description"]) for c in result]
