""" User Model """

from masoniteorm.models import Model
from masoniteorm.scopes import SoftDeletesMixin


class Organization(Model, SoftDeletesMixin):
    """Organization Model"""

    __fillable__ = [
        "name",
        "email",
        "city",
        "phone",
        "address",
        "postal_code",
        "description",
        "logo",
        "brand_image",
        "region",
        "country",
        "account_id",
    ]
