""" User Model """

from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to, belongs_to_many, has_many


class Service(Model):
    """Service Model"""

    __fillable__ = ["name", "price", "duration", "account_id"]

    @belongs_to("account_id", "id")
    def account(self):
        from app.models.Account import Account

        return Account

    @has_many("id", "service_id")
    def appointments(self):
        from app.models.Appointment import Appointment

        return Appointment

    @belongs_to_many
    def staffs(self):
        from app.models.Staff import Staff

        return Staff
