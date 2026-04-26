from balepy.objects import HTTPMethod
import balepy

class AddStickerToSet:
    async def add_sticker_to_set(
            self: "balepy.Client",
            user_id: int,
            name: str,
            png_sticker: str,
            emojis: str
    ) -> dict:
        params = {
            'user_id': user_id, 'name': name,
            'png_sticker': png_sticker, 'emojis': emojis
        }
        return await self.api.execute(name="addStickerToSet", method=HTTPMethod.POST, data=params)
