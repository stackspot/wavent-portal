""" User Model """

from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to, has_many
from masoniteorm.scopes import SoftDeletesMixin


class Client(Model, SoftDeletesMixin):
    """Client Model"""

    __fillable__ = ["name", "email", "phone", "account_id"]
    __visible__ = ["id", "name", "email", "phone", "deleted_at"]

    @has_many("id", "client_id")
    def appointments(self):
        from app.models.Appointment import Appointment

        return Appointment

    @belongs_to("account_id", "id")
    def account(self):
        from app.models.Account import Account

        return Account
