""" Schedule Model """

from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to, belongs_to_many


class Schedule(Model):
    """Schedule Model"""

    __dates__ = ["start_time", "finish_time"]
    __fillable__ = ["start_time", "finish_time"]

    @belongs_to
    def account(self):
        from app.models.Account import Account

        return Account

    @belongs_to_many
    def staff(self):
        from app.models.Staff import Staff

        return Staff
