""" User Model """

from masoniteorm.models import Model


class Service(Model):
    """Service Model"""

    __fillable__ = ["name", "price", "duration"]
