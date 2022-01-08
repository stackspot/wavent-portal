from app.models.Appointment import Appointment
from masonite.controllers import Controller
from masonite.facades import Request, Response, Session
from masonite.inertia import Inertia
from masonite.response import response


class AppointmentsController(Controller):
    def __init__(self, view: Inertia):
        self.view = view
        self.request = Request
        self.response = Response
        self.session = Session

    def index(self):
        appointments = Appointment.all()

        return self.view.render("Appointment/index", {"appointments": appointments})

    def create(self):
        return self.view.render("")

    def store(self):
        # TODO: check if can create appointment

        # TODO: validate the request object
        # TODO: get the services, user(employee), then
        # TODO: create the appointment
        Appointment.create(**self.request.all())

        self.session.flash("success", "Serviço criado.")
        return self.response.redirect("service.index")

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
