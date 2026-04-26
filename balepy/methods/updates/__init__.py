from .get_updates import GetUpdates
from .get_webhook_info import GetWebhookInfo
from .set_webhook import SetWebhook
from .delete_webhook import DeleteWebhook


class Updates(GetUpdates, GetWebhookInfo, SetWebhook, DeleteWebhook):
    pass
