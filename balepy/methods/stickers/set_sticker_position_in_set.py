from balepy.objects import HTTPMethod
import balepy

class SetStickerPositionInSet:
    async def set_sticker_position_in_set(self: "balepy.Client", sticker: str, position: int) -> dict:
        params = {'sticker': sticker, 'position': position}
        return await self.api.execute(name="setStickerPositionInSet", method=HTTPMethod.POST, data=params)
