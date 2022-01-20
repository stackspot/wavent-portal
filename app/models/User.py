"""User Model."""
from masonite.authentication import Authenticates
from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to
from masoniteorm.scopes import SoftDeletesMixin


class User(Model, SoftDeletesMixin, Authenticates):
    """User Model."""

    __fillable__ = ["name", "email", "password", "phone", "is_admin", "account_id"]
    __visible__ = ["id", "name", "email", "phone", "is_admin", "account_id", "deleted_at"]
    __auth__ = "email"

    @belongs_to("account_id", "id")
    def account(self):
        from app.models.Account import Account

        return Account
