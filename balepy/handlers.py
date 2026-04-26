"""
Handler classes for balepy.

Usage:
    from balepy.handlers import MessageHandler, CallbackQueryHandler, CommandHandler
    from balepy import filters

    bot.add_handler(MessageHandler(callback, filters.text & filters.private))
    bot.add_handler(CommandHandler("start", start_callback))
    bot.add_handler(CallbackQueryHandler(callback, data_match="btn_*"))
"""

from __future__ import annotations
from typing import Callable, Optional, Union
import re

from balepy.filters import Filter, CommandFilter


class Handler:
    """Base handler class."""

    def __init__(self, callback: Callable, filters: Optional[Filter] = None):
        self.callback = callback
        self.filters = filters

    def check(self, update_obj) -> bool:
        if self.filters is None:
            return True
        return self.filters.check(update_obj)


class MessageHandler(Handler):
    """Handles message updates."""
    pass


class EditedMessageHandler(Handler):
    """Handles edited message updates."""
    pass


class ChannelPostHandler(Handler):
    """Handles channel post updates."""
    pass


class EditedChannelPostHandler(Handler):
    """Handles edited channel post updates."""
    pass


class CommandHandler(Handler):
    """Handles command messages."""

    def __init__(self, commands: Union[str, list[str]], callback: Callable, prefixes: str = "/"):
        super().__init__(callback, CommandFilter(commands, prefixes))


class CallbackQueryHandler(Handler):
    """Handles callback query updates."""

    def __init__(self, callback: Callable, filters: Optional[Filter] = None,
                 data_match: Optional[str] = None):
        super().__init__(callback, filters)
        self.data_pattern = re.compile(data_match.replace("*", ".*")) if data_match else None

    def check(self, callback_query) -> bool:
        if self.data_pattern:
            data = getattr(callback_query, "data_text", None) or ""
            if not self.data_pattern.match(data):
                return False
        return super().check(callback_query)


class PreCheckoutQueryHandler(Handler):
    """Handles pre-checkout query updates for payments."""
    pass


class ShippingQueryHandler(Handler):
    """Handles shipping query updates."""
    pass


class SuccessfulPaymentHandler(Handler):
    """Handles successful payment updates."""
    pass


class MyChatMemberHandler(Handler):
    """Handles my_chat_member updates."""
    pass


class ChatMemberHandler(Handler):
    """Handles chat_member updates."""
    pass


class ChatJoinRequestHandler(Handler):
    """Handles chat join request updates."""
    pass


class NewChatMembersHandler(Handler):
    """Handles new chat members joining."""
    pass


class LeftChatMemberHandler(Handler):
    """Handles members leaving chat."""
    pass
