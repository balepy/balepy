from __future__ import annotations
from typing import TYPE_CHECKING, Optional

from balepy.types.message import Message
from balepy.types.callback_query import CallbackQuery
from balepy.types._base import PreCheckoutQuery, ShippingQuery, ChatMemberUpdated, ChatJoinRequest

if TYPE_CHECKING:
    import balepy


class Update:

    def __init__(self, data: dict, client: "balepy.Client" = None):
        self.data = data
        self.client = client

    @property
    def update_id(self) -> int:
        return self.data.get("update_id")

    @property
    def message(self) -> Optional[Message]:
        d = self.data.get("message")
        return Message(d, client=self.client) if d else None

    @property
    def callback_query(self) -> Optional[CallbackQuery]:
        d = self.data.get("callback_query")
        return CallbackQuery(d, client=self.client) if d else None

    @property
    def edited_message(self) -> Optional[Message]:
        d = self.data.get("edited_message")
        return Message(d, client=self.client) if d else None

    @property
    def channel_post(self) -> Optional[Message]:
        d = self.data.get("channel_post")
        return Message(d, client=self.client) if d else None

    @property
    def edited_channel_post(self) -> Optional[Message]:
        d = self.data.get("edited_channel_post")
        return Message(d, client=self.client) if d else None

    @property
    def pre_checkout_query(self) -> Optional[PreCheckoutQuery]:
        d = self.data.get("pre_checkout_query")
        return PreCheckoutQuery(d, client=self.client) if d else None

    @property
    def shipping_query(self) -> Optional[ShippingQuery]:
        d = self.data.get("shipping_query")
        return ShippingQuery(d, client=self.client) if d else None

    @property
    def my_chat_member(self) -> Optional[ChatMemberUpdated]:
        d = self.data.get("my_chat_member")
        return ChatMemberUpdated(d) if d else None

    @property
    def chat_member(self) -> Optional[ChatMemberUpdated]:
        d = self.data.get("chat_member")
        return ChatMemberUpdated(d) if d else None

    @property
    def chat_join_request(self) -> Optional[ChatJoinRequest]:
        d = self.data.get("chat_join_request")
        return ChatJoinRequest(d, client=self.client) if d else None

    def __repr__(self) -> str:
        return f"Update(update_id={self.update_id})"


Updates = Update
