from .get_me import GetMe
from .log_out import LogOut
from .ban_chat_member import BanChatMember
from .unban_chat_member import UnbanChatMember
from .promote_chat_member import PromoteChatMember
from .restrict_chat_member import RestrictChatMember
from .set_chat_photo import SetChatPhoto
from .leave_chat import LeaveChat
from .get_chat import GetChat
from .get_user import GetUser
from .get_chat_administrators import GetChatAdministrators
from .get_chat_members_count import GetChatMembersCount
from .get_chat_member import GetChatMember
from .get_user_profile_photos import GetUserProfilePhotos
from .set_chat_title import SetChatTitle
from .set_chat_description import SetChatDescription
from .set_chat_permissions import SetChatPermissions
from .set_chat_administrator_custom_title import SetChatAdministratorCustomTitle
from .delete_chat_photo import DeleteChatPhoto
from .create_chat_invite_link import CreateChatInviteLink
from .edit_chat_invite_link import EditChatInviteLink
from .revoke_chat_invite_link import RevokeChatInviteLink
from .export_chat_invite_link import ExportChatInviteLink
from .approve_chat_join_request import ApproveChatJoinRequest
from .decline_chat_join_request import DeclineChatJoinRequest
from .invite_to_chat import InviteToChat
from .set_my_commands import SetMyCommands
from .get_my_commands import GetMyCommands
from .delete_my_commands import DeleteMyCommands


class Users(GetMe,
            LogOut,
            BanChatMember,
            UnbanChatMember,
            PromoteChatMember,
            RestrictChatMember,
            SetChatPhoto,
            LeaveChat,
            GetChat,
            GetUser,
            GetChatAdministrators,
            GetChatMembersCount,
            GetChatMember,
            GetUserProfilePhotos,
            SetChatTitle,
            SetChatDescription,
            SetChatPermissions,
            SetChatAdministratorCustomTitle,
            DeleteChatPhoto,
            CreateChatInviteLink,
            EditChatInviteLink,
            RevokeChatInviteLink,
            ExportChatInviteLink,
            ApproveChatJoinRequest,
            DeclineChatJoinRequest,
            InviteToChat,
            SetMyCommands,
            GetMyCommands,
            DeleteMyCommands
            ):
    pass
