from masonite.controllers import Controller
from masonite.inertia import Inertia
from masonite.request import Request
from masonite.response import Response
from masonite.views import View


class AppointmentsController(Controller):
    def __init__(self, view: Inertia, request: Request, response: Response):
        self.view = view
        self.request = request
        self.response = response

    def index(self):
        appointments = []
        return self.view.render("Appointment/index")

    def create(self):
        return self.view.render("")

    def store(self):
        # TODO: check if can create appointment
        # TODO: validate the request object
        # TODO: get the services, user(employee), then
        # TODO: create the appointment
        return self.view.render("")

    def show(self):
        # TODO: check if can get the appointment
        # TODO: return the appointment
        return self.view.render("")

    def edit(self):
        # TODO: check if can edit appointment
        # TODO: return the appointment
        return self.view.render("")

    def update(self):
        # TODO: check if can update appointment
        # TODO: validate the request object
        # TODO: get the services, user(employee), then
        # TODO: update the appointment
        return self.view.render("")

    def destroy(self):
        # TODO: check if can delete appointment
        # TODO: delete the appointment
        return self.view.render("")
