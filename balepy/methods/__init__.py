from .users import Users
from .updates import Updates
from .messages import Messages
from .payments import Payments
from .stickers import Stickers


class Methods(Users, Updates, Messages, Payments, Stickers):
    pass
