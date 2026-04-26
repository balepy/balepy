from __future__ import annotations
from typing import Optional, Callable, Union, TYPE_CHECKING
import asyncio
import logging

from balepy.http import API
from balepy.types import Update, Message
from balepy.types._base import PreCheckoutQuery, ShippingQuery, ChatMemberUpdated, ChatJoinRequest
from balepy.types.callback_query import CallbackQuery
from balepy.methods import Methods
from balepy.filters import Filter

try:
    from colorama import Fore
except ImportError:
    class Fore:
        GREEN = RED = YELLOW = RESET = ""

logger = logging.getLogger("balepy")


class _HandlerEntry:

    def __init__(self, callback: Callable, filters: Optional[Filter] = None, group: int = 0):
        self.callback = callback
        self.filters = filters
        self.group = group


class Client(Methods):
    """
    Main client class for Bale bot API.

    Usage:
        from balepy import Client, filters

        bot = Client("MyBot", "TOKEN")

        @bot.on_message(filters.command("start"))
        async def start(message):
            await message.reply("Hello!")

        bot.run()
    """

    def __init__(
            self,
            name: str,
            bot_token: str,
            wallet_token: Optional[str] = None,
            timeout: Optional[int] = 20,
            max_retry: Optional[int] = 3,
            base_url: Optional[str] = None,
            proxies: Optional[str] = None
    ):
        self.name = name
        self.bot_token = bot_token
        self.wallet_token = wallet_token
        self.timeout = timeout
        self.max_retry = max_retry
        self.base_url = base_url
        self.proxies = proxies
        self.api = API(client=self)

        # Pyrogram-style handler lists
        self._message_handlers: list[_HandlerEntry] = []
        self._callback_handlers: list[_HandlerEntry] = []
        self._edited_message_handlers: list[_HandlerEntry] = []
        self._channel_post_handlers: list[_HandlerEntry] = []
        self._edited_channel_post_handlers: list[_HandlerEntry] = []
        self._successful_payment_handlers: list[_HandlerEntry] = []
        self._pre_checkout_query_handlers: list[_HandlerEntry] = []
        self._shipping_query_handlers: list[_HandlerEntry] = []
        self._new_member_handlers: list[_HandlerEntry] = []
        self._left_member_handlers: list[_HandlerEntry] = []
        self._my_chat_member_handlers: list[_HandlerEntry] = []
        self._chat_member_handlers: list[_HandlerEntry] = []
        self._chat_join_request_handlers: list[_HandlerEntry] = []
        self._raw_update_handlers: list[_HandlerEntry] = []

        # Middleware
        self._middlewares: list[Callable] = []

        # Error handler
        self._error_handler: Optional[Callable] = None

        if wallet_token == "WALLET-TEST-1111111111111111":
            print(f"{Fore.RED}WARNING: {Fore.YELLOW}Using TEST WALLET{Fore.RESET}")

    # ============================
    # Decorator-based handlers (Pyrogram style)
    # ============================
    def on_message(self, filters: Optional[Filter] = None, group: int = 0):
        """Decorator for message handlers with optional filters.

        Can be used as:
            @bot.on_message                          # no parens, no filter
            @bot.on_message()                        # empty parens
            @bot.on_message(filters.command("start"))  # with filter
        """
        def decorator(func: Callable) -> Callable:
            self._message_handlers.append(_HandlerEntry(func, filters, group))
            self._message_handlers.sort(key=lambda h: h.group)
            return func
        # If called without parentheses: @bot.on_message
        # Then `filters` is actually the decorated function (not a Filter instance)
        if callable(filters) and not isinstance(filters, Filter):
            func = filters
            self._message_handlers.append(_HandlerEntry(func, None, 0))
            return func
        return decorator

    def on_callback_query(self, filters: Optional[Filter] = None, group: int = 0):
        def decorator(func: Callable) -> Callable:
            self._callback_handlers.append(_HandlerEntry(func, filters, group))
            self._callback_handlers.sort(key=lambda h: h.group)
            return func
        if callable(filters) and not isinstance(filters, Filter):
            func = filters
            self._callback_handlers.append(_HandlerEntry(func, None, 0))
            return func
        return decorator

    def on_edited_message(self, filters: Optional[Filter] = None, group: int = 0):
        def decorator(func: Callable) -> Callable:
            self._edited_message_handlers.append(_HandlerEntry(func, filters, group))
            return func
        if callable(filters) and not isinstance(filters, Filter):
            func = filters
            self._edited_message_handlers.append(_HandlerEntry(func, None, 0))
            return func
        return decorator

    def on_channel_post(self, filters: Optional[Filter] = None, group: int = 0):
        def decorator(func: Callable) -> Callable:
            self._channel_post_handlers.append(_HandlerEntry(func, filters, group))
            return func
        if callable(filters) and not isinstance(filters, Filter):
            func = filters
            self._channel_post_handlers.append(_HandlerEntry(func, None, 0))
            return func
        return decorator

    def on_edited_channel_post(self, filters: Optional[Filter] = None, group: int = 0):
        def decorator(func: Callable) -> Callable:
            self._edited_channel_post_handlers.append(_HandlerEntry(func, filters, group))
            return func
        if callable(filters) and not isinstance(filters, Filter):
            func = filters
            self._edited_channel_post_handlers.append(_HandlerEntry(func, None, 0))
            return func
        return decorator

    def on_successful_payment(self, func: Callable) -> Callable:
        self._successful_payment_handlers.append(_HandlerEntry(func))
        return func

    def on_pre_checkout_query(self, func: Callable) -> Callable:
        self._pre_checkout_query_handlers.append(_HandlerEntry(func))
        return func

    def on_shipping_query(self, func: Callable) -> Callable:
        self._shipping_query_handlers.append(_HandlerEntry(func))
        return func

    def on_new_member(self, func: Callable) -> Callable:
        self._new_member_handlers.append(_HandlerEntry(func))
        return func

    def on_left_member(self, func: Callable) -> Callable:
        self._left_member_handlers.append(_HandlerEntry(func))
        return func

    def on_my_chat_member(self, func: Callable) -> Callable:
        self._my_chat_member_handlers.append(_HandlerEntry(func))
        return func

    def on_chat_member(self, func: Callable) -> Callable:
        self._chat_member_handlers.append(_HandlerEntry(func))
        return func

    def on_chat_join_request(self, func: Callable) -> Callable:
        self._chat_join_request_handlers.append(_HandlerEntry(func))
        return func

    def on_raw_update(self, func: Callable) -> Callable:
        self._raw_update_handlers.append(_HandlerEntry(func))
        return func

    def on_error(self, func: Callable) -> Callable:
        self._error_handler = func
        return func

    # ============================
    # Handler-class registration
    # ============================
    def add_handler(self, handler, group: int = 0):
        """Add handler object from balepy.handlers module."""
        from balepy.handlers import (
            MessageHandler, EditedMessageHandler, ChannelPostHandler,
            EditedChannelPostHandler, CallbackQueryHandler as CQHandler,
            PreCheckoutQueryHandler, ShippingQueryHandler,
            SuccessfulPaymentHandler, MyChatMemberHandler,
            ChatMemberHandler as CMHandler, ChatJoinRequestHandler,
            NewChatMembersHandler, LeftChatMemberHandler, CommandHandler
        )
        entry = _HandlerEntry(handler.callback, handler.filters, group)

        if isinstance(handler, (MessageHandler, CommandHandler)):
            self._message_handlers.append(entry)
            self._message_handlers.sort(key=lambda h: h.group)
        elif isinstance(handler, EditedMessageHandler):
            self._edited_message_handlers.append(entry)
        elif isinstance(handler, ChannelPostHandler):
            self._channel_post_handlers.append(entry)
        elif isinstance(handler, EditedChannelPostHandler):
            self._edited_channel_post_handlers.append(entry)
        elif isinstance(handler, CQHandler):
            self._callback_handlers.append(entry)
        elif isinstance(handler, PreCheckoutQueryHandler):
            self._pre_checkout_query_handlers.append(entry)
        elif isinstance(handler, ShippingQueryHandler):
            self._shipping_query_handlers.append(entry)
        elif isinstance(handler, SuccessfulPaymentHandler):
            self._successful_payment_handlers.append(entry)
        elif isinstance(handler, MyChatMemberHandler):
            self._my_chat_member_handlers.append(entry)
        elif isinstance(handler, CMHandler):
            self._chat_member_handlers.append(entry)
        elif isinstance(handler, ChatJoinRequestHandler):
            self._chat_join_request_handlers.append(entry)
        elif isinstance(handler, NewChatMembersHandler):
            self._new_member_handlers.append(entry)
        elif isinstance(handler, LeftChatMemberHandler):
            self._left_member_handlers.append(entry)

    def remove_handler(self, handler, group: int = 0):
        """Remove a handler."""
        for handler_list in (self._message_handlers, self._callback_handlers,
                            self._edited_message_handlers, self._channel_post_handlers,
                            self._pre_checkout_query_handlers):
            handler_list[:] = [
                h for h in handler_list
                if h.callback != handler.callback
            ]

    # ============================
    # Middleware
    # ============================
    def use(self, middleware: Callable):
        """Add middleware function. Receives (client, update) and returns bool."""
        self._middlewares.append(middleware)

    # ============================
    # Dispatch system
    # ============================
    async def _check_filter(self, filt: Filter, obj) -> bool:
        """Check a filter, supporting both sync and async filters."""
        if hasattr(filt, 'async_check'):
            return await filt.async_check(obj)
        return filt.check(obj)

    async def _run_handlers(self, handlers: list[_HandlerEntry], obj):
        for entry in handlers:
            try:
                if entry.filters is None or await self._check_filter(entry.filters, obj):
                    await entry.callback(obj)
            except Exception as e:
                if self._error_handler:
                    await self._error_handler(e, obj)
                else:
                    logger.error(f"Error in handler: {e}", exc_info=True)

    async def _dispatch(self, update: Update):
        # Run middlewares
        for mw in self._middlewares:
            try:
                result = mw(self, update)
                if asyncio.iscoroutine(result):
                    result = await result
                if result is False:
                    return
            except Exception as e:
                logger.error(f"Middleware error: {e}")

        # Raw update handlers
        for entry in self._raw_update_handlers:
            try:
                await entry.callback(update)
            except Exception as e:
                logger.error(f"Raw handler error: {e}")

        # Callback queries
        if update.callback_query is not None:
            await self._run_handlers(self._callback_handlers, update.callback_query)
            return

        # Pre-checkout query (PAYMENT - CRITICAL: must respond in 10s)
        if update.pre_checkout_query is not None:
            await self._run_handlers(self._pre_checkout_query_handlers, update.pre_checkout_query)
            return

        # Shipping query
        if update.shipping_query is not None:
            await self._run_handlers(self._shipping_query_handlers, update.shipping_query)
            return

        # Edited message
        if update.edited_message is not None:
            await self._run_handlers(self._edited_message_handlers, update.edited_message)
            return

        # Channel post
        if update.channel_post is not None:
            await self._run_handlers(self._channel_post_handlers, update.channel_post)
            return

        # Edited channel post
        if update.edited_channel_post is not None:
            await self._run_handlers(self._edited_channel_post_handlers, update.edited_channel_post)
            return

        # my_chat_member
        if update.my_chat_member is not None:
            await self._run_handlers(self._my_chat_member_handlers, update.my_chat_member)
            return

        # chat_member
        if update.chat_member is not None:
            await self._run_handlers(self._chat_member_handlers, update.chat_member)
            return

        # chat_join_request
        if update.chat_join_request is not None:
            await self._run_handlers(self._chat_join_request_handlers, update.chat_join_request)
            return

        # Message
        msg = update.message
        if msg is None:
            return

        # Successful payment inside message
        if msg.successful_payment is not None:
            await self._run_handlers(self._successful_payment_handlers, msg)
            return

        # New members
        if msg.new_chat_members is not None:
            await self._run_handlers(self._new_member_handlers, msg)
            return

        # Left member
        if msg.left_chat_member is not None:
            await self._run_handlers(self._left_member_handlers, msg)
            return

        # Regular message
        await self._run_handlers(self._message_handlers, msg)

    async def process_update(self):
        offset = -1
        while True:
            try:
                updates = await self.get_updates(offset=offset, limit=100)
                if not isinstance(updates, str) and updates:
                    for raw in updates:
                        offset = raw["update_id"] + 1
                        yield Update(raw, client=self)
            except Exception as e:
                logger.error(f"Polling error: {e}")
                await asyncio.sleep(2)
            await asyncio.sleep(0.3)

    def run(self):
        """Start bot with long polling."""
        async def _runner():
            print(f"{Fore.GREEN}{self.name} is running...{Fore.RESET}")
            async for update in self.process_update():
                asyncio.create_task(self._dispatch(update))
        try:
            asyncio.run(_runner())
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}{self.name} stopped.{Fore.RESET}")

    async def start(self):
        """Start polling (for use inside existing event loop)."""
        print(f"{Fore.GREEN}{self.name} is running...{Fore.RESET}")
        async for update in self.process_update():
            asyncio.create_task(self._dispatch(update))

    def get_file_url(self, file_path: str) -> str:
        """Get direct download URL for a file."""
        base = self.base_url or "https://tapi.bale.ai"
        return f"{base}/file/bot{self.bot_token}/{file_path}"

    async def download_file(self, file_id: str) -> tuple:
        """Download a file by file_id. Returns (file_path, download_url)."""
        file_obj = await self.get_file(file_id)
        fp = file_obj.file_path
        url = self.get_file_url(fp)
        return fp, url
