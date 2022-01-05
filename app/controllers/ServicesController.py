from app.models.Service import Service
from masonite.controllers import Controller
from masonite.inertia import Inertia
from masonite.request import Request
from masonite.response import Response
from masonite.sessions import Session
from masonite.validation import Validator


class ServicesController(Controller):
    def __init__(
        self,
        view: Inertia,
        request: Request,
        session: Session,
        response: Response,
        validate: Validator,
    ):
        self.view = view
        self.request = request
        self.session = session
        self.response = response
        self.validate = validate

    def index(self):
        return self.view.render("Service/index")

    def create(self):
        return self.view.render("Service/create")

    def store(self):
        errors = self.request.validate(
            self.validate.required(
                ["name", "duration", "price"],
                messages={
                    "name": "Tens de escrever o nome do serviço a registrar.(e.g. Corte simples)",
                    "duration": "Forneça a duração do serviço em minutos.(e.g. 45 min.)",
                    "price": "Tens de fornecer o preço do serviço.(e.g. 7€)",
                },
            ),
            self.validate.numeric(["duration"]),
        )

        if errors:
            return self.response.redirect(name="service.index").with_errors(errors).with_input()

        Service.create(
            name=self.request.input("name"),
            duration=self.request.input("duration"),
            price=self.request.input("price"),
            description=self.request.input("description"),
        )
        self.session.flash("success", "Serviço adicionado com sucesso.")
        return self.response.redirect(name="service.index")

    def show(self):
        # service = Service.find(self.request.param("service"))
        return self.view.render("Client/details")

    def edit(self):
        # service = Service.find(self.request.param("service"))
        return self.view.render("Service/edit")

    def update(self):
        self.session.flash("success", "Serviço atualizado com sucesso.")
        return self.response.redirect(name="service.index")

    def destroy(self):
        # service = Service.find(self.request.param("service"))
        # service.delete()
        self.session.flash("success", "Serviço apagado com sucesso.")
        return self.response.redirect(name="service.index")
