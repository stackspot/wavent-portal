from os import name

from app.models.Provider import Provider
from masonite.controllers import Controller
from masonite.filesystem import Storage
from masonite.inertia import Inertia
from masonite.request import Request
from masonite.response import Response
from masonite.sessions import Session
from masonite.validation import Validator


class ProvidersController(Controller):
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
        provider = self.request.user().account.provider

        return self.view.render("Organization/index", {"provider": provider.serialize()})

    def create(self):
        return self.view.render("")

    def store(self):
        errors = self.request.validate(
            self.validate.required(["name", "address", "email"]),
            self.validate.length("phone", max=50),
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

        Provider.create(
            name=self.request.input("name"),
            email=self.request.input("email"),
            phone=self.request.input("phone"),
            address=self.request.input("address"),
            logo=logo,
            brand_image=brand_image,
            account_id=self.request.user().account.id,
        )
        return self.response.redirect(name="org.index")

    def show(self):
        provider = Provider.find(self.request.param("provider"))
        return self.view.render("")

    def edit(self):
        provider = Provider.find(self.request.param("provider"))
        return self.view.render("")

    def update(self):
        provider = Provider.find(self.request.param("provider"))

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

        Provider.update(
            name=self.request.input("name"),
            email=self.request.input("email"),
            phone=self.request.input("phone"),
            address=self.request.input("address"),
            description=self.request.input("description"),
            logo=logo,
            brand_image=brand_image,
            account_id=self.request.user().account.id,
        )
        self.session.flash("success", "Conta criada com sucesso.")
        return self.response.redirect(name="provider.index")

    def destroy(self):
        # provider = self.request.user().providers()
        provider = Provider.find(self.request.param("provider"))
        provider.delete()
        self.session.flash("success", "Conta apagada com sucesso.")
        return self.response.redirect(name="provider.index")
