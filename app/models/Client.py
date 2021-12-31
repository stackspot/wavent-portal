""" User Model """

from masoniteorm.models import Model
from masoniteorm.scopes import SoftDeletesMixin


class Client(Model, SoftDeletesMixin):
    """Client Model"""

    __fillable__ = ["name", "email", "phone"]
