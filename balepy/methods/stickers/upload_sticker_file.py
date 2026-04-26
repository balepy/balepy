from balepy.objects import HTTPMethod
import balepy

class UploadStickerFile:
    async def upload_sticker_file(self: "balepy.Client", user_id: int, png_sticker: str) -> dict:
        params = {'user_id': user_id, 'png_sticker': png_sticker}
        return await self.api.execute(name="uploadStickerFile", method=HTTPMethod.POST, data=params)
