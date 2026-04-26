"""
Filters module for balepy - Pyrogram-style filters for handlers.

Usage:
    from balepy import filters

    @bot.on_message(filters.command("start"))
    async def start(message):
        await message.reply("Hello!")

    @bot.on_message(filters.text & filters.private)
    async def text_handler(message):
        await message.reply(message.text)
"""

from __future__ import annotations
from typing import Callable, Optional, Union
import asyncio
import re


class Filter:
    """Base filter class."""

    def __call__(self, message) -> bool:
        return self.check(message)

    def check(self, message) -> bool:
        raise NotImplementedError

    async def async_check(self, message) -> bool:
        """Async version of check. Override for async filters."""
        return self.check(message)

    def __and__(self, other: Filter) -> AndFilter:
        return AndFilter(self, other)

    def __or__(self, other: Filter) -> OrFilter:
        return OrFilter(self, other)

    def __invert__(self) -> InvertFilter:
        return InvertFilter(self)


class AndFilter(Filter):

    def __init__(self, f1: Filter, f2: Filter):
        self.f1 = f1
        self.f2 = f2

    def check(self, message) -> bool:
        return self.f1.check(message) and self.f2.check(message)

    async def async_check(self, message) -> bool:
        return await self.f1.async_check(message) and await self.f2.async_check(message)


class OrFilter(Filter):

    def __init__(self, f1: Filter, f2: Filter):
        self.f1 = f1
        self.f2 = f2

    def check(self, message) -> bool:
        return self.f1.check(message) or self.f2.check(message)

    async def async_check(self, message) -> bool:
        return await self.f1.async_check(message) or await self.f2.async_check(message)


class InvertFilter(Filter):

    def __init__(self, f: Filter):
        self.f = f

    def check(self, message) -> bool:
        return not self.f.check(message)

    async def async_check(self, message) -> bool:
        return not await self.f.async_check(message)


class _TextFilter(Filter):
    """Matches messages with text content."""

    def check(self, message) -> bool:
        return bool(getattr(message, "text", None))


class _PhotoFilter(Filter):

    def check(self, message) -> bool:
        return bool(getattr(message, "photo", None))


class _VideoFilter(Filter):

    def check(self, message) -> bool:
        return bool(getattr(message, "video", None))


class _AudioFilter(Filter):

    def check(self, message) -> bool:
        return bool(getattr(message, "audio", None))


class _VoiceFilter(Filter):

    def check(self, message) -> bool:
        return bool(getattr(message, "voice", None))


class _DocumentFilter(Filter):

    def check(self, message) -> bool:
        return bool(getattr(message, "document", None))


class _StickerFilter(Filter):

    def check(self, message) -> bool:
        return bool(getattr(message, "sticker", None))


class _AnimationFilter(Filter):

    def check(self, message) -> bool:
        return bool(getattr(message, "animation", None))


class _ContactFilter(Filter):

    def check(self, message) -> bool:
        return bool(getattr(message, "contact", None))


class _LocationFilter(Filter):

    def check(self, message) -> bool:
        return bool(getattr(message, "location", None))


class _DiceFilter(Filter):

    def check(self, message) -> bool:
        return bool(getattr(message, "dice", None))


class _InvoiceFilter(Filter):

    def check(self, message) -> bool:
        return bool(getattr(message, "invoice", None))


class _SuccessfulPaymentFilter(Filter):

    def check(self, message) -> bool:
        return bool(getattr(message, "successful_payment", None))


class _NewChatMembersFilter(Filter):

    def check(self, message) -> bool:
        return bool(getattr(message, "new_chat_members", None))


class _LeftChatMemberFilter(Filter):

    def check(self, message) -> bool:
        return bool(getattr(message, "left_chat_member", None))


class _PinnedMessageFilter(Filter):

    def check(self, message) -> bool:
        return bool(getattr(message, "pinned_message", None))


class _ReplyFilter(Filter):

    def check(self, message) -> bool:
        return bool(getattr(message, "reply_to_message", None))


class _ForwardFilter(Filter):

    def check(self, message) -> bool:
        fwd = getattr(message, "forward_from", None) or getattr(message, "forward_from_chat", None)
        return bool(fwd)


class _PrivateFilter(Filter):

    def check(self, message) -> bool:
        chat = getattr(message, "chat", None)
        if chat:
            return getattr(chat, "type", None) == "private"
        return False


class _GroupFilter(Filter):

    def check(self, message) -> bool:
        chat = getattr(message, "chat", None)
        if chat:
            return getattr(chat, "type", None) in ("group", "supergroup")
        return False


class _ChannelFilter(Filter):

    def check(self, message) -> bool:
        chat = getattr(message, "chat", None)
        if chat:
            return getattr(chat, "type", None) == "channel"
        return False


class _AllFilter(Filter):

    def check(self, message) -> bool:
        return True


class _BotFilter(Filter):

    def check(self, message) -> bool:
        user = getattr(message, "from_user", None)
        if user:
            return getattr(user, "is_bot", False)
        return False


class _VideoNoteFilter(Filter):

    def check(self, message) -> bool:
        return bool(getattr(message, "video_note", None))


class _VenueFilter(Filter):

    def check(self, message) -> bool:
        return bool(getattr(message, "venue", None))


class _CaptionFilter(Filter):

    def check(self, message) -> bool:
        return bool(getattr(message, "caption", None))


class _MediaFilter(Filter):

    def check(self, message) -> bool:
        for field in ("photo", "video", "audio", "document", "voice",
                     "video_note", "animation", "sticker"):
            if getattr(message, field, None):
                return True
        return False


class CommandFilter(Filter):
    """Matches command messages like /start, /help."""

    def __init__(self, commands: Union[str, list[str]], prefixes: str = "/"):
        if isinstance(commands, str):
            commands = [commands]
        self.commands = [c.lower().lstrip("/") for c in commands]
        self.prefixes = prefixes

    def check(self, message) -> bool:
        text = getattr(message, "text", None)
        if not text:
            return False
        if not text[0] in self.prefixes:
            return False
        cmd = text.split()[0][1:].split("@")[0].lower()
        return cmd in self.commands


class RegexFilter(Filter):
    """Matches messages matching a regex pattern."""

    def __init__(self, pattern: str, flags: int = 0):
        self.pattern = re.compile(pattern, flags)

    def check(self, message) -> bool:
        text = getattr(message, "text", None) or getattr(message, "caption", None) or ""
        return bool(self.pattern.search(text))


class TextMatchFilter(Filter):
    """Matches messages containing specific text."""

    def __init__(self, keywords: Union[str, list[str]], case_sensitive: bool = False):
        if isinstance(keywords, str):
            keywords = [keywords]
        self.keywords = keywords
        self.case_sensitive = case_sensitive

    def check(self, message) -> bool:
        text = getattr(message, "text", None) or ""
        if not self.case_sensitive:
            text = text.lower()
            return any(k.lower() in text for k in self.keywords)
        return any(k in text for k in self.keywords)


class UserFilter(Filter):
    """Matches messages from specific users."""

    def __init__(self, user_ids: Union[int, list[int]]):
        if isinstance(user_ids, int):
            user_ids = [user_ids]
        self.user_ids = user_ids

    def check(self, message) -> bool:
        user = getattr(message, "from_user", None)
        if user:
            return getattr(user, "id", None) in self.user_ids
        return False


class ChatFilter(Filter):
    """Matches messages from specific chats."""

    def __init__(self, chat_ids: Union[int, list[int]]):
        if isinstance(chat_ids, int):
            chat_ids = [chat_ids]
        self.chat_ids = chat_ids

    def check(self, message) -> bool:
        chat_id = getattr(message, "chat_id", None)
        return chat_id in self.chat_ids


class CustomFilter(Filter):
    """User-defined custom filter with a callable (sync or async)."""

    def __init__(self, func: Callable):
        self.func = func
        self._is_async = asyncio.iscoroutinefunction(func)

    def check(self, message) -> bool:
        if self._is_async:
            # For async filters, return True and let _run_handlers handle it
            # This is a fallback; prefer using async_check
            return True
        return bool(self.func(message))

    async def async_check(self, message) -> bool:
        if self._is_async:
            return bool(await self.func(message))
        return bool(self.func(message))


class CallbackDataFilter(Filter):
    """Matches callback queries by data pattern."""

    def __init__(self, pattern: Union[str, list[str]]):
        if isinstance(pattern, str):
            self.patterns = [pattern]
        else:
            self.patterns = pattern

    def check(self, obj) -> bool:
        # Support both Message (won't have callback data) and CallbackQuery objects
        data = getattr(obj, "data_text", None) or getattr(obj, "data", None)
        if isinstance(data, dict):
            # If data is the raw dict (CallbackQuery.data is the raw dict), get "data" field
            data = data.get("data") if isinstance(data, dict) else data
        if not data or not isinstance(data, str):
            return False
        for pattern in self.patterns:
            if "*" in pattern:
                regex = re.compile("^" + re.escape(pattern).replace(r"\*", ".*") + "$")
                if regex.match(data):
                    return True
            elif data == pattern:
                return True
        return False


def command(commands: Union[str, list[str]], prefixes: str = "/") -> CommandFilter:
    return CommandFilter(commands, prefixes)


def regex(pattern: str, flags: int = 0) -> RegexFilter:
    return RegexFilter(pattern, flags)


def text_match(keywords: Union[str, list[str]], case_sensitive: bool = False) -> TextMatchFilter:
    return TextMatchFilter(keywords, case_sensitive)


def user(user_ids: Union[int, list[int]]) -> UserFilter:
    return UserFilter(user_ids)


def chat(chat_ids: Union[int, list[int]]) -> ChatFilter:
    return ChatFilter(chat_ids)


def callback_data(pattern: Union[str, list[str]]) -> CallbackDataFilter:
    """Match callback query data. Supports wildcards with '*'."""
    return CallbackDataFilter(pattern)


def create(func: Callable) -> CustomFilter:
    return CustomFilter(func)


# Singleton instances
text = _TextFilter()
photo = _PhotoFilter()
video = _VideoFilter()
audio = _AudioFilter()
voice = _VoiceFilter()
document = _DocumentFilter()
sticker = _StickerFilter()
animation = _AnimationFilter()
contact = _ContactFilter()
location = _LocationFilter()
dice = _DiceFilter()
invoice = _InvoiceFilter()
successful_payment = _SuccessfulPaymentFilter()
new_chat_members = _NewChatMembersFilter()
left_chat_member = _LeftChatMemberFilter()
pinned_message = _PinnedMessageFilter()
reply = _ReplyFilter()
forwarded = _ForwardFilter()
private = _PrivateFilter()
group = _GroupFilter()
channel = _ChannelFilter()
all = _AllFilter()
bot = _BotFilter()
video_note = _VideoNoteFilter()
venue = _VenueFilter()
caption = _CaptionFilter()
media = _MediaFilter()
