from .get_sticker_set import GetStickerSet
from .upload_sticker_file import UploadStickerFile
from .create_new_sticker_set import CreateNewStickerSet
from .add_sticker_to_set import AddStickerToSet
from .delete_sticker_from_set import DeleteStickerFromSet
from .set_sticker_position_in_set import SetStickerPositionInSet


class Stickers(GetStickerSet,
               UploadStickerFile,
               CreateNewStickerSet,
               AddStickerToSet,
               DeleteStickerFromSet,
               SetStickerPositionInSet):
    pass
