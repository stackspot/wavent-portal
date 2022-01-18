from app.models.Appointment import Appointment
from app.models.Service import Service
from app.models.User import User
from masonite.controllers import Controller
from masonite.inertia import Inertia
from masonite.request import Request
from masonite.response import Response, response
from masonite.sessions import Session


class AppointmentsController(Controller):
    def __init__(
        self,
        request: Request,
        response: Response,
        view: Inertia,
        session: Session,
    ):
        self.view = view
        self.request = request
        self.response = response
        self.session = session

    def index(self):
        appointments = self.request.user().account.appointments

        return self.view.render("Appointment/index")

    def create(self):
        return self.view.render("")

    def store(self):
        # TODO: check if can create appointment

        # TODO: validate the request object
        # TODO: get the services, user(employee), then
        # TODO: create the appointment

        service = Service.find(self.request.input("service"))
        Appointment.create(**self.request.only())
        # Appointment.save_many(service)
        print(self.request.all())
        self.session.flash("success", "Marcação criado com sucesso.")
        return self.response.redirect(name="appointment.index")

    def show(self):
        # TODO: check if can get the appointment
        # TODO: return the appointment
        appointment = Appointment.find(self.request.param("appointment"))

        return self.response.json({"appoinment": appointment.serialize()})

    def edit(self):
        # TODO: check if can edit appointment
        # TODO: return the appointment
        appointment = Appointment.find(self.request.param("appointment"))

        return self.response.json({"appoinment": appointment.serialize()})

    def update(self):
        # TODO: check if can update appointment
        # TODO: validate the request object
        # TODO: get the services, user(employee), then
        # TODO: update the appointment
        appointment = Appointment.find(self.request.param("appointment"))

        appointment.update(**self.request.all())

        return self.response.json({"appoinment": appointment.serialize()})

    def destroy(self):
        # TODO: check if can delete appointment
        # TODO: delete the appointment
        return self.view.render("")
