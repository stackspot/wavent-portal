""" Provider Model """

from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to
from masoniteorm.scopes import SoftDeletesMixin


class Provider(Model, SoftDeletesMixin):
    """Provider Model"""

    __fillable__ = [
        "name",
        "email",
        "phone",
        "address",
        "description",
        "logo",
        "brand_image",
        "account_id",
    ]

    @belongs_to
    def account(self):
        from app.models.Account import Account
        return Account
