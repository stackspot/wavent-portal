""" User Model """

from masoniteorm.models import Model


class Appointment(Model):
    """Appointment Model"""

    __dates__ = ["start_time", "finish_time"]
    __fillable__ = ["start_time", "finish_time", "client_id", "client_name", "client_email", "client_phone", "account_id", "price", "is_noshow", "canceled", "cancellation_reason"]
