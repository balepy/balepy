from __future__ import annotations
from typing import Optional, Union
import json


class User:

    def __init__(self, data: dict):
        self.data = data.get("result", data)

    @property
    def id(self) -> int:
        return self.data.get("id")

    @property
    def is_bot(self) -> bool:
        return self.data.get("is_bot")

    @property
    def first_name(self) -> str:
        return self.data.get("first_name")

    @property
    def last_name(self) -> Optional[str]:
        return self.data.get("last_name")

    @property
    def username(self) -> Optional[str]:
        return self.data.get("username")

    @property
    def language_code(self) -> Optional[str]:
        return self.data.get("language_code")

    def __repr__(self) -> str:
        return f"User(id={self.id}, first_name={self.first_name!r})"


class ChatPhoto:

    def __init__(self, data: dict):
        self.data = data or {}

    @property
    def small_file_id(self) -> str:
        return self.data.get("small_file_id")

    @property
    def small_file_unique_id(self) -> str:
        return self.data.get("small_file_unique_id")

    @property
    def big_file_id(self) -> str:
        return self.data.get("big_file_id")

    @property
    def big_file_unique_id(self) -> str:
        return self.data.get("big_file_unique_id")


class Chat:

    def __init__(self, data: dict):
        self.data = data.get("result", data)

    @property
    def id(self) -> int:
        return self.data.get("id")

    @property
    def type(self) -> str:
        return self.data.get("type")

    @property
    def title(self) -> Optional[str]:
        return self.data.get("title")

    @property
    def username(self) -> Optional[str]:
        return self.data.get("username")

    @property
    def first_name(self) -> Optional[str]:
        return self.data.get("first_name")

    @property
    def last_name(self) -> Optional[str]:
        return self.data.get("last_name")

    def __repr__(self) -> str:
        return f"Chat(id={self.id}, type={self.type!r})"


class ChatFullInfo:

    def __init__(self, data: dict):
        self.data = data.get("result", data)

    @property
    def id(self) -> int:
        return self.data.get("id")

    @property
    def type(self) -> str:
        return self.data.get("type")

    @property
    def title(self) -> Optional[str]:
        return self.data.get("title")

    @property
    def username(self) -> Optional[str]:
        return self.data.get("username")

    @property
    def first_name(self) -> Optional[str]:
        return self.data.get("first_name")

    @property
    def last_name(self) -> Optional[str]:
        return self.data.get("last_name")

    @property
    def photo(self) -> Optional[ChatPhoto]:
        d = self.data.get("photo")
        return ChatPhoto(d) if d else None

    @property
    def bio(self) -> Optional[str]:
        return self.data.get("bio")

    @property
    def description(self) -> Optional[str]:
        return self.data.get("description")

    @property
    def invite_link(self) -> Optional[str]:
        return self.data.get("invite_link")

    @property
    def pinned_message(self) -> Optional[dict]:
        return self.data.get("pinned_message")

    @property
    def linked_chat_id(self) -> Optional[int]:
        return self.data.get("linked_chat_id")

    @property
    def sticker_set_name(self) -> Optional[str]:
        return self.data.get("sticker_set_name")

    @property
    def can_set_sticker_set(self) -> Optional[bool]:
        return self.data.get("can_set_sticker_set")


class MessageEntity:

    def __init__(self, data: dict):
        self.data = data

    @property
    def type(self) -> str:
        return self.data.get("type")

    @property
    def offset(self) -> int:
        return self.data.get("offset")

    @property
    def length(self) -> int:
        return self.data.get("length")

    @property
    def url(self) -> Optional[str]:
        return self.data.get("url")

    @property
    def user(self) -> Optional[User]:
        d = self.data.get("user")
        return User(d) if d else None

    @property
    def language(self) -> Optional[str]:
        return self.data.get("language")


class PhotoSize:

    def __init__(self, data: dict):
        self.data = data

    @property
    def file_id(self) -> str:
        return self.data.get("file_id")

    @property
    def file_unique_id(self) -> str:
        return self.data.get("file_unique_id")

    @property
    def width(self) -> int:
        return self.data.get("width")

    @property
    def height(self) -> int:
        return self.data.get("height")

    @property
    def file_size(self) -> Optional[int]:
        return self.data.get("file_size")


class Audio:

    def __init__(self, data: dict):
        self.data = data

    @property
    def file_id(self) -> str:
        return self.data.get("file_id")

    @property
    def file_unique_id(self) -> str:
        return self.data.get("file_unique_id")

    @property
    def duration(self) -> int:
        return self.data.get("duration")

    @property
    def performer(self) -> Optional[str]:
        return self.data.get("performer")

    @property
    def title(self) -> Optional[str]:
        return self.data.get("title")

    @property
    def file_name(self) -> Optional[str]:
        return self.data.get("file_name")

    @property
    def mime_type(self) -> Optional[str]:
        return self.data.get("mime_type")

    @property
    def file_size(self) -> Optional[int]:
        return self.data.get("file_size")

    @property
    def thumb(self) -> Optional[PhotoSize]:
        d = self.data.get("thumb")
        return PhotoSize(d) if d else None


class Document:

    def __init__(self, data: dict):
        self.data = data

    @property
    def file_id(self) -> str:
        return self.data.get("file_id")

    @property
    def file_unique_id(self) -> str:
        return self.data.get("file_unique_id")

    @property
    def file_name(self) -> Optional[str]:
        return self.data.get("file_name")

    @property
    def mime_type(self) -> Optional[str]:
        return self.data.get("mime_type")

    @property
    def file_size(self) -> Optional[int]:
        return self.data.get("file_size")

    @property
    def thumb(self) -> Optional[PhotoSize]:
        d = self.data.get("thumb")
        return PhotoSize(d) if d else None


class Video:

    def __init__(self, data: dict):
        self.data = data

    @property
    def file_id(self) -> str:
        return self.data.get("file_id")

    @property
    def file_unique_id(self) -> str:
        return self.data.get("file_unique_id")

    @property
    def width(self) -> int:
        return self.data.get("width")

    @property
    def height(self) -> int:
        return self.data.get("height")

    @property
    def duration(self) -> int:
        return self.data.get("duration")

    @property
    def file_name(self) -> Optional[str]:
        return self.data.get("file_name")

    @property
    def mime_type(self) -> Optional[str]:
        return self.data.get("mime_type")

    @property
    def file_size(self) -> Optional[int]:
        return self.data.get("file_size")

    @property
    def thumb(self) -> Optional[PhotoSize]:
        d = self.data.get("thumb")
        return PhotoSize(d) if d else None


class Voice:

    def __init__(self, data: dict):
        self.data = data

    @property
    def file_id(self) -> str:
        return self.data.get("file_id")

    @property
    def file_unique_id(self) -> str:
        return self.data.get("file_unique_id")

    @property
    def duration(self) -> int:
        return self.data.get("duration")

    @property
    def mime_type(self) -> Optional[str]:
        return self.data.get("mime_type")

    @property
    def file_size(self) -> Optional[int]:
        return self.data.get("file_size")


class VideoNote:

    def __init__(self, data: dict):
        self.data = data

    @property
    def file_id(self) -> str:
        return self.data.get("file_id")

    @property
    def file_unique_id(self) -> str:
        return self.data.get("file_unique_id")

    @property
    def length(self) -> int:
        return self.data.get("length")

    @property
    def duration(self) -> int:
        return self.data.get("duration")

    @property
    def thumb(self) -> Optional[PhotoSize]:
        d = self.data.get("thumb")
        return PhotoSize(d) if d else None

    @property
    def file_size(self) -> Optional[int]:
        return self.data.get("file_size")


class Animation:

    def __init__(self, data: dict):
        self.data = data

    @property
    def file_id(self) -> str:
        return self.data.get("file_id")

    @property
    def file_unique_id(self) -> str:
        return self.data.get("file_unique_id")

    @property
    def width(self) -> int:
        return self.data.get("width")

    @property
    def height(self) -> int:
        return self.data.get("height")

    @property
    def duration(self) -> int:
        return self.data.get("duration")

    @property
    def file_name(self) -> Optional[str]:
        return self.data.get("file_name")

    @property
    def mime_type(self) -> Optional[str]:
        return self.data.get("mime_type")

    @property
    def file_size(self) -> Optional[int]:
        return self.data.get("file_size")

    @property
    def thumb(self) -> Optional[PhotoSize]:
        d = self.data.get("thumb")
        return PhotoSize(d) if d else None


class Sticker:

    def __init__(self, data: dict):
        self.data = data

    @property
    def file_id(self) -> str:
        return self.data.get("file_id")

    @property
    def file_unique_id(self) -> str:
        return self.data.get("file_unique_id")

    @property
    def width(self) -> int:
        return self.data.get("width")

    @property
    def height(self) -> int:
        return self.data.get("height")

    @property
    def is_animated(self) -> Optional[bool]:
        return self.data.get("is_animated")

    @property
    def emoji(self) -> Optional[str]:
        return self.data.get("emoji")

    @property
    def set_name(self) -> Optional[str]:
        return self.data.get("set_name")

    @property
    def thumb(self) -> Optional[PhotoSize]:
        d = self.data.get("thumb")
        return PhotoSize(d) if d else None

    @property
    def file_size(self) -> Optional[int]:
        return self.data.get("file_size")


class StickerSet:

    def __init__(self, data: dict):
        self.data = data.get("result", data)

    @property
    def name(self) -> str:
        return self.data.get("name")

    @property
    def title(self) -> str:
        return self.data.get("title")

    @property
    def is_animated(self) -> bool:
        return self.data.get("is_animated", False)

    @property
    def contains_masks(self) -> bool:
        return self.data.get("contains_masks", False)

    @property
    def stickers(self) -> list[Sticker]:
        return [Sticker(s) for s in self.data.get("stickers", [])]


class Contact:

    def __init__(self, data: dict):
        self.data = data

    @property
    def phone_number(self) -> str:
        return self.data.get("phone_number")

    @property
    def first_name(self) -> str:
        return self.data.get("first_name")

    @property
    def last_name(self) -> Optional[str]:
        return self.data.get("last_name")

    @property
    def user_id(self) -> Optional[int]:
        return self.data.get("user_id")

    @property
    def vcard(self) -> Optional[str]:
        return self.data.get("vcard")


class Location:

    def __init__(self, data: dict):
        self.data = data

    @property
    def longitude(self) -> float:
        return self.data.get("longitude")

    @property
    def latitude(self) -> float:
        return self.data.get("latitude")

    @property
    def horizontal_accuracy(self) -> Optional[float]:
        return self.data.get("horizontal_accuracy")


class Dice:

    def __init__(self, data: dict):
        self.data = data

    @property
    def emoji(self) -> str:
        return self.data.get("emoji")

    @property
    def value(self) -> int:
        return self.data.get("value")


class File:

    def __init__(self, data: dict):
        self.data = data.get("result", data)

    @property
    def file_id(self) -> str:
        return self.data.get("file_id")

    @property
    def file_unique_id(self) -> str:
        return self.data.get("file_unique_id")

    @property
    def file_size(self) -> Optional[int]:
        return self.data.get("file_size")

    @property
    def file_path(self) -> Optional[str]:
        return self.data.get("file_path")


class WebHookInfo:

    def __init__(self, data: dict):
        self.data = data.get("result", data)

    @property
    def url(self) -> Optional[str]:
        return self.data.get("url")

    @property
    def has_custom_certificate(self) -> Optional[bool]:
        return self.data.get("has_custom_certificate")

    @property
    def pending_update_count(self) -> Optional[int]:
        return self.data.get("pending_update_count")

    @property
    def last_error_date(self) -> Optional[int]:
        return self.data.get("last_error_date")

    @property
    def last_error_message(self) -> Optional[str]:
        return self.data.get("last_error_message")

    @property
    def max_connections(self) -> Optional[int]:
        return self.data.get("max_connections")

    @property
    def allowed_updates(self) -> Optional[list[str]]:
        return self.data.get("allowed_updates")


class LabeledPrice:

    def __init__(self, label: str, amount: int):
        self.label = label
        self.amount = amount

    def to_dict(self) -> dict:
        return {"label": self.label, "amount": self.amount}


class Invoice:

    def __init__(self, data: dict):
        self.data = data

    @property
    def title(self) -> str:
        return self.data.get("title")

    @property
    def description(self) -> str:
        return self.data.get("description")

    @property
    def start_parameter(self) -> Optional[str]:
        return self.data.get("start_parameter")

    @property
    def currency(self) -> str:
        return self.data.get("currency")

    @property
    def total_amount(self) -> int:
        return self.data.get("total_amount")


class OrderInfo:

    def __init__(self, data: dict):
        self.data = data

    @property
    def name(self) -> Optional[str]:
        return self.data.get("name")

    @property
    def phone_number(self) -> Optional[str]:
        return self.data.get("phone_number")

    @property
    def email(self) -> Optional[str]:
        return self.data.get("email")


class SuccessfulPayment:

    def __init__(self, data: dict):
        self.data = data

    @property
    def currency(self) -> str:
        return self.data.get("currency")

    @property
    def total_amount(self) -> int:
        return self.data.get("total_amount")

    @property
    def invoice_payload(self) -> str:
        return self.data.get("invoice_payload")

    @property
    def telegram_payment_charge_id(self) -> str:
        return self.data.get("telegram_payment_charge_id")

    @property
    def provider_payment_charge_id(self) -> str:
        return self.data.get("provider_payment_charge_id")

    @property
    def order_info(self) -> Optional[OrderInfo]:
        d = self.data.get("order_info")
        return OrderInfo(d) if d else None


class PreCheckoutQuery:

    def __init__(self, data: dict, client=None):
        self.data = data
        self.client = client

    @property
    def id(self) -> str:
        return self.data.get("id")

    @property
    def from_user(self) -> Optional[User]:
        d = self.data.get("from")
        return User(d) if d else None

    @property
    def currency(self) -> str:
        return self.data.get("currency")

    @property
    def total_amount(self) -> int:
        return self.data.get("total_amount")

    @property
    def invoice_payload(self) -> str:
        return self.data.get("invoice_payload")

    @property
    def order_info(self) -> Optional[OrderInfo]:
        d = self.data.get("order_info")
        return OrderInfo(d) if d else None

    async def answer(self, ok: bool = True, error_message: Optional[str] = None) -> dict:
        return await self.client.answer_pre_checkout_query(
            pre_checkout_query_id=self.id,
            ok=ok,
            error_message=error_message
        )


class ShippingAddress:

    def __init__(self, data: dict):
        self.data = data

    @property
    def country_code(self) -> str:
        return self.data.get("country_code")

    @property
    def state(self) -> str:
        return self.data.get("state")

    @property
    def city(self) -> str:
        return self.data.get("city")

    @property
    def street_line1(self) -> str:
        return self.data.get("street_line1")

    @property
    def street_line2(self) -> str:
        return self.data.get("street_line2")

    @property
    def post_code(self) -> str:
        return self.data.get("post_code")


class ShippingQuery:

    def __init__(self, data: dict, client=None):
        self.data = data
        self.client = client

    @property
    def id(self) -> str:
        return self.data.get("id")

    @property
    def from_user(self) -> Optional[User]:
        d = self.data.get("from")
        return User(d) if d else None

    @property
    def invoice_payload(self) -> str:
        return self.data.get("invoice_payload")

    @property
    def shipping_address(self) -> Optional[ShippingAddress]:
        d = self.data.get("shipping_address")
        return ShippingAddress(d) if d else None


class InputMediaPhoto:

    def __init__(self, media: str, caption: Optional[str] = None):
        self.media = media
        self.caption = caption

    def to_dict(self) -> dict:
        d = {"type": "photo", "media": self.media}
        if self.caption:
            d["caption"] = self.caption
        return d


class InputMediaVideo:

    def __init__(
            self,
            media: str,
            caption: Optional[str] = None,
            width: Optional[int] = None,
            height: Optional[int] = None,
            duration: Optional[int] = None
    ):
        self.media = media
        self.caption = caption
        self.width = width
        self.height = height
        self.duration = duration

    def to_dict(self) -> dict:
        d = {"type": "video", "media": self.media}
        if self.caption:
            d["caption"] = self.caption
        if self.width:
            d["width"] = self.width
        if self.height:
            d["height"] = self.height
        if self.duration:
            d["duration"] = self.duration
        return d


class InputMediaDocument:

    def __init__(self, media: str, caption: Optional[str] = None):
        self.media = media
        self.caption = caption

    def to_dict(self) -> dict:
        d = {"type": "document", "media": self.media}
        if self.caption:
            d["caption"] = self.caption
        return d


class InputMediaAudio:

    def __init__(
            self,
            media: str,
            caption: Optional[str] = None,
            duration: Optional[int] = None,
            performer: Optional[str] = None,
            title: Optional[str] = None
    ):
        self.media = media
        self.caption = caption
        self.duration = duration
        self.performer = performer
        self.title = title

    def to_dict(self) -> dict:
        d = {"type": "audio", "media": self.media}
        if self.caption:
            d["caption"] = self.caption
        if self.duration:
            d["duration"] = self.duration
        if self.performer:
            d["performer"] = self.performer
        if self.title:
            d["title"] = self.title
        return d


class ChatMember:

    def __init__(self, data: dict):
        self.data = data.get("result", data)

    @property
    def user(self) -> Optional[User]:
        d = self.data.get("user")
        return User(d) if d else None

    @property
    def status(self) -> str:
        return self.data.get("status")

    @property
    def custom_title(self) -> Optional[str]:
        return self.data.get("custom_title")

    @property
    def can_be_edited(self) -> Optional[bool]:
        return self.data.get("can_be_edited")

    @property
    def can_change_info(self) -> Optional[bool]:
        return self.data.get("can_change_info")

    @property
    def can_post_messages(self) -> Optional[bool]:
        return self.data.get("can_post_messages")

    @property
    def can_edit_messages(self) -> Optional[bool]:
        return self.data.get("can_edit_messages")

    @property
    def can_delete_messages(self) -> Optional[bool]:
        return self.data.get("can_delete_messages")

    @property
    def can_invite_users(self) -> Optional[bool]:
        return self.data.get("can_invite_users")

    @property
    def can_restrict_members(self) -> Optional[bool]:
        return self.data.get("can_restrict_members")

    @property
    def can_pin_messages(self) -> Optional[bool]:
        return self.data.get("can_pin_messages")

    @property
    def can_promote_members(self) -> Optional[bool]:
        return self.data.get("can_promote_members")

    @property
    def can_manage_video_chats(self) -> Optional[bool]:
        return self.data.get("can_manage_video_chats")

    @property
    def is_anonymous(self) -> Optional[bool]:
        return self.data.get("is_anonymous")

    @property
    def until_date(self) -> Optional[int]:
        return self.data.get("until_date")


class ChatMemberUpdated:

    def __init__(self, data: dict):
        self.data = data

    @property
    def chat(self) -> Optional[Chat]:
        d = self.data.get("chat")
        return Chat(d) if d else None

    @property
    def from_user(self) -> Optional[User]:
        d = self.data.get("from")
        return User(d) if d else None

    @property
    def date(self) -> int:
        return self.data.get("date")

    @property
    def old_chat_member(self) -> Optional[ChatMember]:
        d = self.data.get("old_chat_member")
        return ChatMember(d) if d else None

    @property
    def new_chat_member(self) -> Optional[ChatMember]:
        d = self.data.get("new_chat_member")
        return ChatMember(d) if d else None

    @property
    def invite_link(self) -> Optional[InviteLink]:
        d = self.data.get("invite_link")
        return InviteLink(d) if d else None


class ChatJoinRequest:

    def __init__(self, data: dict, client=None):
        self.data = data
        self.client = client

    @property
    def chat(self) -> Optional[Chat]:
        d = self.data.get("chat")
        return Chat(d) if d else None

    @property
    def from_user(self) -> Optional[User]:
        d = self.data.get("from")
        return User(d) if d else None

    @property
    def date(self) -> int:
        return self.data.get("date")

    @property
    def bio(self) -> Optional[str]:
        return self.data.get("bio")

    @property
    def invite_link(self) -> Optional[InviteLink]:
        d = self.data.get("invite_link")
        return InviteLink(d) if d else None


class InviteLink:

    def __init__(self, data: dict):
        self.data = data.get("result", data)

    @property
    def invite_link(self) -> Optional[str]:
        return self.data.get("invite_link") if isinstance(self.data, dict) else self.data

    @property
    def creator(self) -> Optional[User]:
        d = self.data.get("creator") if isinstance(self.data, dict) else None
        return User(d) if d else None

    @property
    def is_primary(self) -> Optional[bool]:
        return self.data.get("is_primary") if isinstance(self.data, dict) else None

    @property
    def is_revoked(self) -> Optional[bool]:
        return self.data.get("is_revoked") if isinstance(self.data, dict) else None

    @property
    def expire_date(self) -> Optional[int]:
        return self.data.get("expire_date") if isinstance(self.data, dict) else None

    @property
    def member_limit(self) -> Optional[int]:
        return self.data.get("member_limit") if isinstance(self.data, dict) else None

    @property
    def creates_join_request(self) -> Optional[bool]:
        return self.data.get("creates_join_request") if isinstance(self.data, dict) else None

    @property
    def name(self) -> Optional[str]:
        return self.data.get("name") if isinstance(self.data, dict) else None

    @property
    def pending_join_request_count(self) -> Optional[int]:
        return self.data.get("pending_join_request_count") if isinstance(self.data, dict) else None


class WebAppInfo:

    def __init__(self, url: str):
        self.url = url

    def to_dict(self) -> dict:
        return {"url": self.url}


class InlineKeyboardButton:

    def __init__(
            self,
            text: str,
            callback_data: Optional[str] = None,
            url: Optional[str] = None,
            web_app: Optional[WebAppInfo] = None,
            switch_inline_query: Optional[str] = None,
            switch_inline_query_current_chat: Optional[str] = None
    ):
        self.text = text
        self.callback_data = callback_data
        self.url = url
        self.web_app = web_app
        self.switch_inline_query = switch_inline_query
        self.switch_inline_query_current_chat = switch_inline_query_current_chat

    def to_dict(self) -> dict:
        d = {"text": self.text}
        if self.callback_data is not None:
            d["callback_data"] = self.callback_data
        if self.url is not None:
            d["url"] = self.url
        if self.web_app is not None:
            d["web_app"] = self.web_app.to_dict()
        if self.switch_inline_query is not None:
            d["switch_inline_query"] = self.switch_inline_query
        if self.switch_inline_query_current_chat is not None:
            d["switch_inline_query_current_chat"] = self.switch_inline_query_current_chat
        return d


class InlineKeyboardMarkup:

    def __init__(self, inline_keyboard: Optional[list[list[InlineKeyboardButton]]] = None):
        self.inline_keyboard = inline_keyboard or []

    def add(self, *buttons: InlineKeyboardButton) -> InlineKeyboardMarkup:
        self.inline_keyboard.append(list(buttons))
        return self

    def row(self, *buttons: InlineKeyboardButton) -> InlineKeyboardMarkup:
        self.inline_keyboard.append(list(buttons))
        return self

    def to_dict(self) -> dict:
        return {
            "inline_keyboard": [
                [btn.to_dict() for btn in row]
                for row in self.inline_keyboard
            ]
        }

    def __str__(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False)


class KeyboardButton:

    def __init__(
            self,
            text: str,
            request_contact: bool = False,
            request_location: bool = False,
            web_app: Optional[WebAppInfo] = None
    ):
        self.text = text
        self.request_contact = request_contact
        self.request_location = request_location
        self.web_app = web_app

    def to_dict(self) -> dict:
        d = {"text": self.text}
        if self.request_contact:
            d["request_contact"] = self.request_contact
        if self.request_location:
            d["request_location"] = self.request_location
        if self.web_app is not None:
            d["web_app"] = self.web_app.to_dict()
        return d


class ReplyKeyboardMarkup:

    def __init__(
            self,
            keyboard: Optional[list[list[KeyboardButton]]] = None,
            resize_keyboard: bool = False,
            one_time_keyboard: bool = False,
            selective: bool = False,
            input_field_placeholder: Optional[str] = None
    ):
        self.keyboard = keyboard or []
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.selective = selective
        self.input_field_placeholder = input_field_placeholder

    def add(self, *buttons: KeyboardButton) -> ReplyKeyboardMarkup:
        self.keyboard.append(list(buttons))
        return self

    def row(self, *buttons: KeyboardButton) -> ReplyKeyboardMarkup:
        self.keyboard.append(list(buttons))
        return self

    def to_dict(self) -> dict:
        d = {
            "keyboard": [
                [btn.to_dict() for btn in row]
                for row in self.keyboard
            ],
            "resize_keyboard": self.resize_keyboard,
            "one_time_keyboard": self.one_time_keyboard,
            "selective": self.selective
        }
        if self.input_field_placeholder:
            d["input_field_placeholder"] = self.input_field_placeholder
        return d

    def __str__(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False)


class ReplyKeyboardRemove:

    def __init__(self, selective: bool = False):
        self.selective = selective

    def to_dict(self) -> dict:
        return {
            "remove_keyboard": True,
            "selective": self.selective
        }

    def __str__(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False)


class ForceReply:

    def __init__(
            self,
            selective: bool = False,
            input_field_placeholder: Optional[str] = None
    ):
        self.selective = selective
        self.input_field_placeholder = input_field_placeholder

    def to_dict(self) -> dict:
        d = {
            "force_reply": True,
            "selective": self.selective
        }
        if self.input_field_placeholder:
            d["input_field_placeholder"] = self.input_field_placeholder
        return d

    def __str__(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False)


class BotCommand:

    def __init__(self, command: str, description: str):
        self.command = command
        self.description = description

    def to_dict(self) -> dict:
        return {"command": self.command, "description": self.description}


class ChatPermissions:

    def __init__(
            self,
            can_send_messages: Optional[bool] = None,
            can_send_media_messages: Optional[bool] = None,
            can_send_other_messages: Optional[bool] = None,
            can_add_web_page_previews: Optional[bool] = None,
            can_send_link_message: Optional[bool] = None,
            can_send_forwarded_message: Optional[bool] = None,
            can_reply_to_story: Optional[bool] = None,
            can_see_members: Optional[bool] = None,
            can_add_story: Optional[bool] = None,
    ):
        self.can_send_messages = can_send_messages
        self.can_send_media_messages = can_send_media_messages
        self.can_send_other_messages = can_send_other_messages
        self.can_add_web_page_previews = can_add_web_page_previews
        self.can_send_link_message = can_send_link_message
        self.can_send_forwarded_message = can_send_forwarded_message
        self.can_reply_to_story = can_reply_to_story
        self.can_see_members = can_see_members
        self.can_add_story = can_add_story

    def to_dict(self) -> dict:
        d = {}
        for key in ("can_send_messages", "can_send_media_messages",
                    "can_send_other_messages", "can_add_web_page_previews",
                    "can_send_link_message", "can_send_forwarded_message",
                    "can_reply_to_story", "can_see_members", "can_add_story"):
            val = getattr(self, key)
            if val is not None:
                d[key] = val
        return d


class Venue:

    def __init__(self, data: dict):
        self.data = data

    @property
    def location(self) -> Optional[Location]:
        d = self.data.get("location")
        return Location(d) if d else None

    @property
    def title(self) -> str:
        return self.data.get("title")

    @property
    def address(self) -> str:
        return self.data.get("address")

    @property
    def foursquare_id(self) -> Optional[str]:
        return self.data.get("foursquare_id")

    @property
    def foursquare_type(self) -> Optional[str]:
        return self.data.get("foursquare_type")


class UserProfilePhotos:

    def __init__(self, data: dict):
        self.data = data.get("result", data)

    @property
    def total_count(self) -> int:
        return self.data.get("total_count", 0)

    @property
    def photos(self) -> list[list[PhotoSize]]:
        return [
            [PhotoSize(p) for p in row]
            for row in self.data.get("photos", [])
        ]


class InputFile:
    """Represents a file to upload. Can be file_id, URL, or local path."""

    def __init__(self, file: str):
        self.file = file

    @property
    def is_file_id(self) -> bool:
        return not self.file.startswith(("http://", "https://", "/", "."))

    @property
    def is_url(self) -> bool:
        return self.file.startswith(("http://", "https://"))

    @property
    def is_local(self) -> bool:
        return not self.is_file_id and not self.is_url

    def __str__(self) -> str:
        return self.file

    def __repr__(self) -> str:
        return f"InputFile({self.file!r})"


class LoginUrl:

    def __init__(self, url: str, forward_text: Optional[str] = None,
                 bot_username: Optional[str] = None):
        self.url = url
        self.forward_text = forward_text
        self.bot_username = bot_username

    def to_dict(self) -> dict:
        d = {"url": self.url}
        if self.forward_text:
            d["forward_text"] = self.forward_text
        if self.bot_username:
            d["bot_username"] = self.bot_username
        return d


class BotCommandScope:

    def __init__(self, type: str, chat_id: Optional[Union[int, str]] = None,
                 user_id: Optional[int] = None):
        self.type = type
        self.chat_id = chat_id
        self.user_id = user_id

    def to_dict(self) -> dict:
        d = {"type": self.type}
        if self.chat_id is not None:
            d["chat_id"] = self.chat_id
        if self.user_id is not None:
            d["user_id"] = self.user_id
        return d

    @staticmethod
    def default() -> BotCommandScope:
        return BotCommandScope("default")

    @staticmethod
    def all_private_chats() -> BotCommandScope:
        return BotCommandScope("all_private_chats")

    @staticmethod
    def all_group_chats() -> BotCommandScope:
        return BotCommandScope("all_group_chats")

    @staticmethod
    def all_chat_administrators() -> BotCommandScope:
        return BotCommandScope("all_chat_administrators")

    @staticmethod
    def chat_scope(chat_id: Union[int, str]) -> BotCommandScope:
        return BotCommandScope("chat", chat_id=chat_id)

    @staticmethod
    def chat_administrators(chat_id: Union[int, str]) -> BotCommandScope:
        return BotCommandScope("chat_administrators", chat_id=chat_id)

    @staticmethod
    def chat_member_scope(chat_id: Union[int, str], user_id: int) -> BotCommandScope:
        return BotCommandScope("chat_member", chat_id=chat_id, user_id=user_id)
