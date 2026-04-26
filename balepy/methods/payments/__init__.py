from .send_invoice import SendInvoice
from .create_invoice_link import CreateInvoiceLink
from .answer_pre_checkout_query import AnswerPreCheckoutQuery
from .answer_shipping_query import AnswerShippingQuery


class Payments(SendInvoice,
               CreateInvoiceLink,
               AnswerPreCheckoutQuery,
               AnswerShippingQuery):
    pass
