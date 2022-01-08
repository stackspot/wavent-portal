""" User Model """

from masoniteorm.models import Model


class Schedule(Model):
    """Schedule Model"""

    __dates__ = ["start_time", "finish_time"]
    __fillable__ = ["start_time", "finish_time"]
