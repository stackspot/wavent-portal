from os import name

from app.models import Organization
from masonite.controllers import Controller
from masonite.filesystem import Storage
from masonite.inertia import Inertia
from masonite.request import Request
from masonite.response import Response
from masonite.sessions import Session
from masonite.validation import Validator


class OrganizationsController(Controller):
    def __init__(
        self,
        request: Request,
        response: Response,
        view: Inertia,
        validate: Validator,
        session: Session,
        storage: Storage,
    ):
        self.request = request
        self.response = response
        self.validate = validate
        self.session = session
        self.view = view
        self.storage = storage

    def index(self):
        # organizations = Organization.all()

        return self.view.render("Organization/index")

    def create(self):
        return self.view.render("")

    def store(self):
        errors = self.request.validate(
            self.validate.required(["name"]),
            self.validate.length(["email", "phone", "city", "region"], max=50),
            self.validate.length(["name"], min=2),
        )
        if errors:
            return self.response.redirect(name="account.create").with_errors(errors).with_input()

        logo = None
        if self.request.input("logo"):
            # save file
            logo = self.storage.disk.put_file("logo", self.request.input("logo"))
        brand_image = None
        if self.request.input("brand_image"):
            # save file
            brand_image = self.storage.disk.put_file("brands", self.request.input("brand_image"))

        """  Organization.create(
            **self.request.only(
                "name", "email", "phone", "address", "city", "region", "country", "postal_code"
            ),
            logo=logo,
            brand_image=brand_image,
            # account_id=self.request.user().account_id,
        ) """
        return self.response.redirect(name="org.index")

    def show(self):
        # organization = self.request.user().organizations()
        organization = Organization.find(self.request.param("organization"))
        return self.view.render("")

    def edit(self):
        organization = Organization.find(self.request.param("organization"))
        return self.view.render("")

    def update(self):
        # organization = self.request.user().organizations()
        organization = Organization.find(self.request.param("organization"))

        errors = self.request.validate(
            self.validate.required(["name"]),
            self.validate.length(["email", "phone", "city", "region"], max=50),
            self.validate.length(["name"], min=2),
        )
        if errors:
            return self.response.redirect(name="account.create").with_errors(errors).with_input()

        logo = None
        if self.request.input("logo"):
            # save file
            logo = self.storage.disk.put_file("logo", self.request.input("logo"))
        brand_image = None
        if self.request.input("brand_image"):
            # save file
            brand_image = self.storage.disk.put_file("brands", self.request.input("brand_image"))

        organization.update(
            **self.request.only(
                "name", "email", "phone", "address", "city", "region", "country", "postal_code"
            ),
            logo=logo,
            brand_image=brand_image,
            # account_id=self.request.user().account_id,
        )
        self.session.flash("success", "Conta criada com sucesso.")
        return self.response.redirect(name="organization.index")

    def destroy(self):
        # organization = self.request.user().organizations()
        organization = Organization.find(self.request.param("organization"))
        organization.delete()
        self.session.flash("success", "Conta apagada com sucesso.")
        return self.response.redirect(name="organization.index")
