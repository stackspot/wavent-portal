""" Account Model """

from masoniteorm.models import Model
from masoniteorm.relationships import has_many, has_one


class Account(Model):
    """Account Model"""

    __fillable__ = ["name", "slug"]

    @has_many
    def appointments(self):
        from app.models.Appointment import Appointment

        return Appointment

    @has_many
    def staffs(self):
        from app.models.Staff import Staff

        return Staff

    @has_many
    def users(self):
        from app.models.User import User

        return User

    @has_many
    def clients(self):
        from app.models.Client import Client

        return Client

    @has_many
    def services(self):
        from app.models.Service import Service

        return Service

    @has_many
    def schedules(self):
        from app.models.Schedule import Schedule

        return Schedule

    @has_one
    def provider(self):
        from app.models.Provider import Provider

        return Provider
