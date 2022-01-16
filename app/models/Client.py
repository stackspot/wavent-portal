""" User Model """

from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to, has_many
from masoniteorm.scopes import SoftDeletesMixin


class Client(Model, SoftDeletesMixin):
    """Client Model"""

    __fillable__ = ["name", "email", "phone"]

    @has_many
    def appointments(self):
        from app.models.Appointment import Appointment

        return Appointment

    @belongs_to
    def account(self):
        from app.models.Account import Account

        return Account
