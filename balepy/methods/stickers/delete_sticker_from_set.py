from balepy.objects import HTTPMethod
import balepy

class DeleteStickerFromSet:
    async def delete_sticker_from_set(self: "balepy.Client", sticker: str) -> dict:
        params = {'sticker': sticker}
        return await self.api.execute(name="deleteStickerFromSet", method=HTTPMethod.POST, data=params)
