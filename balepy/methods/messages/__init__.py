from .send_message import SendMessage
from .forward_message import ForwardMessage
from .copy_message import CopyMessage
from .delete_message import DeleteMessage
from .edit_message_text import EditMessageText
from .send_photo import SendPhoto
from .send_audio import SendAudio
from .send_document import SendDocument
from .send_video import SendVideo
from .send_animation import SendAnimation
from .send_voice import SendVoice
from .send_sticker import SendSticker
from .send_media_group import SendMediaGroup
from .send_location import SendLocation
from .send_contact import SendContact
from .send_chat_action import SendChatAction
from .send_dice import SendDice
from .send_video_note import SendVideoNote
from .send_venue import SendVenue
from .get_file import GetFile
from .anwser_callback_query import AnwserCallbackQuery
from .ask_review import AskReview
from .pin import PinChatMessage
from .unpin import UnpinChatMessage
from .unpin_all_messages import UnpinAllChatMessages
from .edit_message_caption import EditMessageCaption
from .edit_message_reply_markup import EditMessageReplyMarkup


class Messages(SendMessage,
               ForwardMessage,
               CopyMessage,
               DeleteMessage,
               EditMessageText,
               SendPhoto,
               SendAudio,
               SendDocument,
               SendVideo,
               SendAnimation,
               SendVoice,
               SendSticker,
               SendMediaGroup,
               SendLocation,
               SendContact,
               SendChatAction,
               SendDice,
               SendVideoNote,
               SendVenue,
               GetFile,
               AnwserCallbackQuery,
               AskReview,
               PinChatMessage,
               UnpinChatMessage,
               UnpinAllChatMessages,
               EditMessageCaption,
               EditMessageReplyMarkup
               ):
    pass
