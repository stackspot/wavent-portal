from app.models.Client import Client
from masonite.controllers import Controller
from masonite.inertia import Inertia
from masonite.request import Request
from masonite.response import Response
from masonite.sessions import Session
from masonite.validation import Validator


class ClientsController(Controller):
    def __init__(
        self,
        request: Request,
        response: Response,
        view: Inertia,
        validate: Validator,
        session: Session,
    ):
        self.request = request
        self.response = response
        self.view = view
        self.validate = validate
        self.session = session

    def index(self):
        client = Client.all()

        return self.view.render("Client/index")

    def create(self):
        return self.view.render("Client/create")

    def store(self):
        errors = self.request.validate(
            self.validate.required(["name", "email", "phone"]), self.validate.email("email")
        )

        if errors:
            self.session.flash("error", "Houve um error ao criar o cliente.")
            return self.response.redirect(name="client.index").with_errors(errors).with_input()
        Client.create(**self.request.only("name", "email", "phone"))

        self.session.flash("success", "Cliente adicionado com sucesso.")
        return self.response.redirect(name="client.index")

    def show(self):
        client = Client.find(self.request.param("client_id"))

        if not client:
            self.response.redirect(name="client.index").with_errors("Cliente não existe!")

        return self.view.render("Client/details")

    def edit(self):
        client = Client.find(self.request.param("client_id"))

        if not client:
            self.response.redirect(name="client.index").with_errors("Cliente não existe!")

        return self.view.render("Client/edit")

    def update(self):
        client = Client.find(self.request.param("client_id"))

        if not client:
            self.response.redirect(name="client.index").with_errors("Cliente não existe!")

        errors = self.request.validate(
            self.validate.required(["name", "email", "phone"]), self.validate.email("email")
        )

        if errors:
            self.session.flash("error", "Houve um error ao atualizar o cliente.")
            return self.response.redirect(name="client").with_errors(errors).with_input()

        client.update(**self.request.only("name", "email", "phone"))

        self.session.flash("success", "Cliente atualizado com sucesso.")
        return self.response.redirect(name="client.index")

    def destroy(self):
        client = Client.find(self.request.param("client_id"))

        if not client:
            self.response.redirect(name="client.index").with_errors("Cliente não existe!")

        client.delete()
        self.session.flash("success", "Cliente apagado com sucesso.")
        return self.response.redirect(name="client.index")
