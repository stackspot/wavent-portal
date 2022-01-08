from app.models.Service import Service
from masonite.controllers import Controller
from masonite.facades import Request, Response, Session
from masonite.inertia import Inertia
from masonite.validation import Validator


class ServicesController(Controller):
    def __init__(self, view: Inertia, validate: Validator):
        self.view = view
        self.request = Request
        self.session = Session
        self.response = Response
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
            return self.response.redirect(name="service.create").with_input().with_errors(errors)

        try:
            Service.create(**self.request.only("name", "duration", "price"))

        except Exception as e:
            return self.response.redirect(name="service.create").with_input().with_errors(e)

        self.session.flash("success", "Serviço adicionado com sucesso.")
        return self.response.redirect(name="service.index")

    def show(self):

        service = Service.find(self.request.param("service"))

        if not service:
            self.response.status(404), "service not found"

        return self.view.render("Client/details", {"service": service})

    def edit(self):
        service = Service.find(self.request.param("service"))

        if not service:
            self.response.status(404), "service not found"

        return self.view.render("Service/edit", {"service": service})

    def update(self):
        service = Service.find(self.request.param("service"))

        if not service:
            return self.response.status(404)

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
            self.session.flash("errors", errors)
            return self.response.redirect(name="service.edit").with_input()

        service.update(**self.request.only("name", "duration", "price"))

        self.session.flash("success", "Serviço atualizado com sucesso.")
        return self.response.redirect(name="service.index")

    def destroy(self):
        service = Service.find(self.request.param("service"))

        if not service:
            return self.response.status(404)

        service.delete()

        self.session.flash("success", "Serviço apagado com sucesso.")
        return self.response.redirect(name="service.index")
