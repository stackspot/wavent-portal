""" User Model """

from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to, belongs_to_many
from masoniteorm.scopes import scope


class Appointment(Model):
    """Appointment Model"""

    __with__ = ["services", "client", "staff"]

    __dates__ = ["start_time", "finish_time"]
    __fillable__ = [
        "start_time",
        "finish_time",
        "client_id",
        "client_name",
        "client_email",
        "client_phone",
        "price",
        "is_noshow",
        "canceled",
        "cancellation_reason",
        "account_id",
        "staff_id",
    ]

    __hidden__ = ["account_id"]
    __casts__ = {"price": "float"}

    @belongs_to("account_id", "id")
    def accounts(self):
        from app.models.Account import Account

        return Account

    @belongs_to("client_id", "id")
    def client(self):
        from app.models.Client import Client

        return Client

    @belongs_to("staff_id", "id")
    def staff(self):
        from app.models.Staff import Staff

        return Staff

    @belongs_to_many(
        "appointment_id",
        "service_id",
        "id",
        "id",
        table="appointment_service",
        with_timestamps=True,
        attribute="service_provided",
    )
    def services(self):
        from app.models.Service import Service

        return Service
