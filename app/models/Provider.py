""" Provider Model """

from masonite.helpers import url
from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to
from masoniteorm.scopes import SoftDeletesMixin


class Provider(Model):
    """Provider Model"""

    __appends__ = ["logo_path"]

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
    __visible__ = [
        "name",
        "email",
        "phone",
        "address",
        "description",
        "logo_path",
        "brand_image",
        "id",
    ]

    @belongs_to("account_id", "id")
    def account(self):
        from app.models.Account import Account

        return Account

    def get_logo_path_attribute(self):
        return f"/uploads/{self.logo}"
