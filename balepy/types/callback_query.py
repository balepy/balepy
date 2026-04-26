from __future__ import annotations
from typing import TYPE_CHECKING, Optional

from balepy.types._base import User
from balepy.types.message import Message

if TYPE_CHECKING:
    import balepy


class CallbackQuery:

    def __init__(self, data: dict, client: "balepy.Client" = None):
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
    def message(self) -> Optional[Message]:
        d = self.data.get("message")
        return Message(d, client=self.client) if d else None

    @property
    def chat_id(self) -> Optional[int]:
        d = self.data.get("message")
        return d.get("chat", {}).get("id") if d else None

    @property
    def inline_message_id(self) -> Optional[str]:
        return self.data.get("inline_message_id")

    @property
    def chat_instance(self) -> Optional[str]:
        return self.data.get("chat_instance")

    @property
    def data_text(self) -> Optional[str]:
        return self.data.get("data")

    async def answer(self, text: Optional[str] = None, show_alert: bool = False) -> dict:
        return await self.client.anwser_callback_query(
            callback_query_id=self.id, text=text, show_alert=show_alert
        )

    async def reply(self, text: str, reply_markup: Optional[dict] = None) -> Message:
        result = await self.client.send_message(
            chat_id=self.chat_id, text=text, reply_markup=reply_markup
        )
        return Message(result["result"], client=self.client)

    async def edit_text(self, text: str, reply_markup: Optional[dict] = None) -> Message:
        msg = self.message
        result = await self.client.edit_message_text(
            chat_id=self.chat_id, message_id=msg.message_id if msg else None,
            text=text, reply_markup=reply_markup
        )
        return Message(result["result"], client=self.client)

    async def edit_caption(self, caption: Optional[str] = None, reply_markup: Optional[dict] = None) -> Message:
        msg = self.message
        result = await self.client.edit_message_caption(
            chat_id=self.chat_id, message_id=msg.message_id if msg else None,
            caption=caption, reply_markup=reply_markup
        )
        return Message(result["result"], client=self.client)

    async def edit_reply_markup(self, reply_markup: Optional[dict] = None) -> Message:
        msg = self.message
        result = await self.client.edit_message_reply_markup(
            chat_id=self.chat_id, message_id=msg.message_id if msg else None,
            reply_markup=reply_markup
        )
        return Message(result["result"], client=self.client)

    async def delete_message(self) -> dict:
        msg = self.message
        if msg:
            return await self.client.delete_message(
                chat_id=self.chat_id, message_id=msg.message_id
            )
        return {}
