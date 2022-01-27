""" User Model """

from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to, has_many


class Staff(Model):
    """Staff Model"""

    __fillable__ = ["name", "email", "phone", "account_id"]
    __visible__ = ["id", "name", "email", "phone", "deleted_at"]

    @belongs_to("account_id", "id")
    def account(self):
        from app.models.Account import Account

        return Account

    @has_many("id", "staff_id")
    def services(self):
        from app.models.Service import Service

        return Service

    @has_many("id", "staff_id")
    def schedules(self):
        from app.models.Schedule import Schedule

        return Schedule
