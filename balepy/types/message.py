from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Union

from balepy.types._base import (
    User, Chat, MessageEntity, PhotoSize, Audio, Document, Video,
    Voice, VideoNote, Animation, Sticker, Contact, Location, Dice,
    Invoice, SuccessfulPayment, Venue
)

if TYPE_CHECKING:
    import balepy


class Message:

    def __init__(self, data: dict, client: "balepy.Client" = None):
        self.data = data
        self.client = client

    @property
    def message_id(self) -> int:
        return self.data.get("message_id")

    @property
    def from_user(self) -> Optional[User]:
        d = self.data.get("from")
        return User(d) if d else None

    @property
    def chat(self) -> Optional[Chat]:
        d = self.data.get("chat")
        return Chat(d) if d else None

    @property
    def chat_id(self) -> Optional[int]:
        d = self.data.get("chat")
        return d.get("id") if d else None

    @property
    def date(self) -> int:
        return self.data.get("date")

    @property
    def edit_date(self) -> Optional[int]:
        return self.data.get("edit_date")

    @property
    def text(self) -> Optional[str]:
        return self.data.get("text")

    @property
    def entities(self) -> Optional[list[MessageEntity]]:
        ents = self.data.get("entities")
        return [MessageEntity(e) for e in ents] if ents else None

    @property
    def caption(self) -> Optional[str]:
        return self.data.get("caption")

    @property
    def caption_entities(self) -> Optional[list[MessageEntity]]:
        ents = self.data.get("caption_entities")
        return [MessageEntity(e) for e in ents] if ents else None

    @property
    def photo(self) -> Optional[list[PhotoSize]]:
        photos = self.data.get("photo")
        return [PhotoSize(p) for p in photos] if photos else None

    @property
    def audio(self) -> Optional[Audio]:
        d = self.data.get("audio")
        return Audio(d) if d else None

    @property
    def document(self) -> Optional[Document]:
        d = self.data.get("document")
        return Document(d) if d else None

    @property
    def video(self) -> Optional[Video]:
        d = self.data.get("video")
        return Video(d) if d else None

    @property
    def voice(self) -> Optional[Voice]:
        d = self.data.get("voice")
        return Voice(d) if d else None

    @property
    def video_note(self) -> Optional[VideoNote]:
        d = self.data.get("video_note")
        return VideoNote(d) if d else None

    @property
    def animation(self) -> Optional[Animation]:
        d = self.data.get("animation")
        return Animation(d) if d else None

    @property
    def sticker(self) -> Optional[Sticker]:
        d = self.data.get("sticker")
        return Sticker(d) if d else None

    @property
    def contact(self) -> Optional[Contact]:
        d = self.data.get("contact")
        return Contact(d) if d else None

    @property
    def location(self) -> Optional[Location]:
        d = self.data.get("location")
        return Location(d) if d else None

    @property
    def dice(self) -> Optional[Dice]:
        d = self.data.get("dice")
        return Dice(d) if d else None

    @property
    def invoice(self) -> Optional[Invoice]:
        d = self.data.get("invoice")
        return Invoice(d) if d else None

    @property
    def successful_payment(self) -> Optional[SuccessfulPayment]:
        d = self.data.get("successful_payment")
        return SuccessfulPayment(d) if d else None

    @property
    def venue(self) -> Optional[Venue]:
        d = self.data.get("venue")
        return Venue(d) if d else None

    @property
    def reply_to_message(self) -> Optional[Message]:
        d = self.data.get("reply_to_message")
        return Message(d, client=self.client) if d else None

    @property
    def forward_from(self) -> Optional[User]:
        d = self.data.get("forward_from")
        return User(d) if d else None

    @property
    def forward_from_chat(self) -> Optional[Chat]:
        d = self.data.get("forward_from_chat")
        return Chat(d) if d else None

    @property
    def forward_from_message_id(self) -> Optional[int]:
        return self.data.get("forward_from_message_id")

    @property
    def forward_date(self) -> Optional[int]:
        return self.data.get("forward_date")

    @property
    def new_chat_members(self) -> Optional[list[User]]:
        members = self.data.get("new_chat_members")
        return [User(m) for m in members] if members else None

    @property
    def left_chat_member(self) -> Optional[User]:
        d = self.data.get("left_chat_member")
        return User(d) if d else None

    @property
    def new_chat_title(self) -> Optional[str]:
        return self.data.get("new_chat_title")

    @property
    def new_chat_photo(self) -> Optional[list[PhotoSize]]:
        photos = self.data.get("new_chat_photo")
        return [PhotoSize(p) for p in photos] if photos else None

    @property
    def delete_chat_photo(self) -> Optional[bool]:
        return self.data.get("delete_chat_photo")

    @property
    def group_chat_created(self) -> Optional[bool]:
        return self.data.get("group_chat_created")

    @property
    def pinned_message(self) -> Optional[Message]:
        d = self.data.get("pinned_message")
        return Message(d, client=self.client) if d else None

    @property
    def is_reply(self) -> bool:
        return "reply_to_message" in self.data

    @property
    def is_forward(self) -> bool:
        return "forward_from" in self.data or "forward_from_chat" in self.data

    @property
    def content_type(self) -> Optional[str]:
        for key in ("text", "photo", "video", "audio", "document", "voice",
                    "video_note", "animation", "sticker", "contact", "location",
                    "dice", "invoice", "successful_payment", "new_chat_members",
                    "left_chat_member", "new_chat_title", "new_chat_photo",
                    "delete_chat_photo", "group_chat_created", "pinned_message"):
            if key in self.data:
                return key
        return None

    async def reply(self, text: str, reply_markup: Optional[dict] = None) -> Message:
        result = await self.client.send_message(
            chat_id=self.chat_id, text=text,
            reply_to_message_id=self.message_id, reply_markup=reply_markup
        )
        return Message(result["result"], client=self.client)

    async def reply_photo(self, photo: str, caption: Optional[str] = None, reply_markup: Optional[dict] = None) -> Message:
        result = await self.client.send_photo(
            chat_id=self.chat_id, photo=photo, caption=caption,
            reply_to_message_id=self.message_id, reply_markup=reply_markup
        )
        return Message(result["result"], client=self.client)

    async def reply_document(self, document: str, caption: Optional[str] = None, reply_markup: Optional[dict] = None) -> Message:
        result = await self.client.send_document(
            chat_id=self.chat_id, document=document, caption=caption,
            reply_to_message_id=self.message_id, reply_markup=reply_markup
        )
        return Message(result["result"], client=self.client)

    async def reply_audio(self, audio: str, caption: Optional[str] = None, reply_markup: Optional[dict] = None) -> Message:
        result = await self.client.send_audio(
            chat_id=self.chat_id, audio=audio, caption=caption,
            reply_to_message_id=self.message_id, reply_markup=reply_markup
        )
        return Message(result["result"], client=self.client)

    async def reply_video(self, video: str, caption: Optional[str] = None, reply_markup: Optional[dict] = None) -> Message:
        result = await self.client.send_video(
            chat_id=self.chat_id, video=video, caption=caption,
            reply_to_message_id=self.message_id, reply_markup=reply_markup
        )
        return Message(result["result"], client=self.client)

    async def reply_voice(self, voice: str, caption: Optional[str] = None, reply_markup: Optional[dict] = None) -> Message:
        result = await self.client.send_voice(
            chat_id=self.chat_id, voice=voice, caption=caption,
            reply_to_message_id=self.message_id, reply_markup=reply_markup
        )
        return Message(result["result"], client=self.client)

    async def reply_animation(self, animation: str, caption: Optional[str] = None, reply_markup: Optional[dict] = None) -> Message:
        result = await self.client.send_animation(
            chat_id=self.chat_id, animation=animation, caption=caption,
            reply_to_message_id=self.message_id, reply_markup=reply_markup
        )
        return Message(result["result"], client=self.client)

    async def reply_sticker(self, sticker: str, reply_markup: Optional[dict] = None) -> Message:
        result = await self.client.send_sticker(
            chat_id=self.chat_id, sticker=sticker,
            reply_to_message_id=self.message_id, reply_markup=reply_markup
        )
        return Message(result["result"], client=self.client)

    async def reply_video_note(self, video_note: str, reply_markup: Optional[dict] = None) -> Message:
        result = await self.client.send_video_note(
            chat_id=self.chat_id, video_note=video_note,
            reply_to_message_id=self.message_id, reply_markup=reply_markup
        )
        return Message(result["result"], client=self.client)

    async def reply_venue(self, latitude: float, longitude: float, title: str, address: str, reply_markup: Optional[dict] = None) -> Message:
        result = await self.client.send_venue(
            chat_id=self.chat_id, latitude=latitude, longitude=longitude,
            title=title, address=address,
            reply_to_message_id=self.message_id, reply_markup=reply_markup
        )
        return Message(result["result"], client=self.client)

    async def reply_location(self, latitude: float, longitude: float, reply_markup: Optional[dict] = None) -> Message:
        result = await self.client.send_location(
            chat_id=self.chat_id, latitude=latitude, longitude=longitude,
            reply_to_message_id=self.message_id, reply_markup=reply_markup
        )
        return Message(result["result"], client=self.client)

    async def reply_contact(self, phone_number: str, first_name: str, last_name: Optional[str] = None, reply_markup: Optional[dict] = None) -> Message:
        result = await self.client.send_contact(
            chat_id=self.chat_id, phone_number=phone_number, first_name=first_name,
            last_name=last_name, reply_to_message_id=self.message_id, reply_markup=reply_markup
        )
        return Message(result["result"], client=self.client)

    async def forward(self, to_chat_id: Union[int, str]) -> Message:
        result = await self.client.forward_message(
            chat_id=to_chat_id, from_chat_id=self.chat_id, message_id=self.message_id
        )
        return Message(result["result"], client=self.client)

    async def copy_to(self, chat_id: Union[int, str]) -> Message:
        result = await self.client.copy_message(
            chat_id=chat_id, from_chat_id=self.chat_id, message_id=self.message_id
        )
        return Message(result["result"], client=self.client)

    async def delete(self) -> dict:
        return await self.client.delete_message(
            chat_id=self.chat_id, message_id=self.message_id
        )

    async def edit_text(self, text: str, reply_markup: Optional[dict] = None) -> Message:
        result = await self.client.edit_message_text(
            chat_id=self.chat_id, message_id=self.message_id,
            text=text, reply_markup=reply_markup
        )
        return Message(result["result"], client=self.client)

    async def edit_caption(self, caption: Optional[str] = None, reply_markup: Optional[dict] = None) -> Message:
        result = await self.client.edit_message_caption(
            chat_id=self.chat_id, message_id=self.message_id,
            caption=caption, reply_markup=reply_markup
        )
        return Message(result["result"], client=self.client)

    async def edit_reply_markup(self, reply_markup: Optional[dict] = None) -> Message:
        result = await self.client.edit_message_reply_markup(
            chat_id=self.chat_id, message_id=self.message_id, reply_markup=reply_markup
        )
        return Message(result["result"], client=self.client)

    async def pin(self, disable_notification: bool = False) -> dict:
        return await self.client.pin(
            chat_id=self.chat_id, message_id=self.message_id,
            disable_notification=disable_notification
        )

    async def unpin(self) -> dict:
        return await self.client.unpin(
            chat_id=self.chat_id, message_id=self.message_id
        )

    def __repr__(self) -> str:
        return f"Message(message_id={self.message_id}, chat_id={self.chat_id})"
