from typing import Optional
from balepy.objects import HTTPMethod
import balepy

class CreateNewStickerSet:
    async def create_new_sticker_set(
            self: "balepy.Client",
            user_id: int,
            name: str,
            title: str,
            png_sticker: str,
            emojis: str,
            contains_masks: Optional[bool] = None
    ) -> dict:
        params = {
            'user_id': user_id, 'name': name, 'title': title,
            'png_sticker': png_sticker, 'emojis': emojis,
            'contains_masks': contains_masks
        }
        return await self.api.execute(name="createNewStickerSet", method=HTTPMethod.POST, data=params)
