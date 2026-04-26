from balepy.objects import HTTPMethod
from balepy.types import StickerSet
import balepy

class GetStickerSet:
    async def get_sticker_set(self: "balepy.Client", name: str) -> StickerSet:
        params = {'name': name}
        response = await self.api.execute(name="getStickerSet", method=HTTPMethod.POST, data=params)
        return StickerSet(response)
