""" User Model """

from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to, has_many


class Staff(Model):
    """Staff Model"""

    @belongs_to
    def account(self):
        from app.models.Account import Account

        return Account

    @has_many
    def services(self):
        from app.models.Service import Service

        return Service

    @has_many
    def schedules(self):
        from app.models.Schedule import Schedule

        return Schedule
