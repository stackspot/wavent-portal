""" Schedule Model """

from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to, belongs_to_many


class Schedule(Model):
    """Schedule Model"""

    __dates__ = ["start_time", "finish_time"]
    __fillable__ = ["name", "start_time", "finish_time", "is_working", "account_id"]
    __visible__ = ["id", "name", "start_time", "finish_time", "is_working"]

    @belongs_to("account_id", "id")
    def account(self):
        from app.models.Account import Account

        return Account

    @belongs_to_many("schedule_id", "staff_id", "id", "id")
    def staff(self):
        from app.models.Staff import Staff

        return Staff
