"""User Model."""
from masonite.authentication import Authenticates
from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to
from masoniteorm.scopes import SoftDeletesMixin


class User(Model, SoftDeletesMixin, Authenticates):
    """User Model."""

    __fillable__ = ["name", "email", "password", "phone", "is_admin"]
    __hidden__ = ["password"]
    __auth__ = "email"

    @belongs_to
    def account(self):
        from app.models.Account import Account

        return Account
