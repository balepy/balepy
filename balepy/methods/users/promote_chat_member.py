from typing import Optional, Union

from balepy.objects import HTTPMethod

import balepy


class PromoteChatMember:

    async def promote_chat_member(
            self: "balepy.Client",
            chat_id: Union[int, str],
            user_id: int,
            is_anonymous: Optional[bool] = None,
            can_change_info: Optional[bool] = None,
            can_post_messages: Optional[bool] = None,
            can_edit_messages: Optional[bool] = None,
            can_delete_messages: Optional[bool] = None,
            can_manage_video_chats: Optional[bool] = None,
            can_invite_users: Optional[bool] = None,
            can_restrict_members: Optional[bool] = None,
            can_pin_messages: Optional[bool] = None,
            can_promote_members: Optional[bool] = None
    ) -> dict:
        params = {
            'chat_id': chat_id,
            'user_id': user_id,
            'is_anonymous': is_anonymous,
            'can_change_info': can_change_info,
            'can_post_messages': can_post_messages,
            'can_edit_messages': can_edit_messages,
            'can_delete_messages': can_delete_messages,
            'can_manage_video_chats': can_manage_video_chats,
            'can_invite_users': can_invite_users,
            'can_restrict_members': can_restrict_members,
            'can_pin_messages': can_pin_messages,
            'can_promote_members': can_promote_members
        }
        return await self.api.execute(name="promoteChatMember", method=HTTPMethod.POST, data=params)
