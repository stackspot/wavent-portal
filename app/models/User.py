"""User Model."""
from masonite.authentication import Authenticates
from masoniteorm.models import Model
from masoniteorm.scopes import SoftDeletesMixin


class User(Model, SoftDeletesMixin, Authenticates):
    """User Model."""

    __fillable__ = ["name", "email", "password", "phone"]
    __hidden__ = ["password"]
    __auth__ = "email"
