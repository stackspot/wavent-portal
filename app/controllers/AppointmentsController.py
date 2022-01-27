import pendulum
from app.models.Appointment import Appointment
from masonite.controllers import Controller
from masonite.inertia import Inertia
from masonite.request import Request
from masonite.response import Response
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

    @staticmethod
    def format_client(appointment):
        return {
            "name": appointment.client.name
            if appointment.client.name
            else appointment.client_name,
            "email": appointment.client.email
            if appointment.client.email
            else appointment.client_email,
            "phone": appointment.client.phone
            if appointment.client.phone
            else appointment.client_phone,
        }

    @staticmethod
    def format_staff(appointment):
        return {
            "name": appointment.staff.name if appointment.staff.name else "",
            "email": appointment.staff.email if appointment.staff.email else "",
            "phone": appointment.staff.phone if appointment.staff.phone else "",
        }

    @staticmethod
    def get_services(appointment):
        return [
            {
                "name": service.name,
                "price": service.price,
                "duration": service.duration.to_datetime_string(),
            }
            for service in appointment.services
        ]

    def api(self):
        appointments = (
            self.request.user()
            .account.appointments.map(
                lambda appointment: {
                    "client": self.format_client(appointment),
                    "services": self.get_services(appointment),
                    "staff": self.format_staff(appointment),
                    "start_time": appointment.start_time.to_datetime_string(),
                    "finish_time": appointment.finish_time.to_datetime_string(),
                    "price": appointment.price,
                    "id": appointment.id,
                }
            )
            .all()
        )
        return self.response.json({"appointments": appointments})

    def index(self):
        staffs = (
            self.request.user()
            .account.staffs.map(lambda staff: {"label": staff.name, "value": staff.id})
            .all()
        )
        services = (
            self.request.user()
            .account.services.map(lambda service: {"label": service.name, "value": service.id})
            .all()
        )
        clients = (
            self.request.user()
            .account.clients.map(lambda client: {"label": client.name, "value": client.id})
            .all()
        )

        appointments = (
            self.request.user()
            .account.appointments.map(
                lambda appointment: {
                    "client": self.format_client(appointment),
                    "services": self.get_services(appointment),
                    "staff": self.format_staff(appointment),
                    "start_time": appointment.start_time.to_datetime_string(),
                    "finish_time": appointment.finish_time.to_datetime_string(),
                    "price": appointment.price,
                    "id": appointment.id,
                }
            )
            .all()
        )
        return self.view.render(
            "Calendar/index",
            {
                "staffs": staffs,
                "services": services,
                "clients": clients,
                "appointments": appointments,
            },
        )

    def create(self):
        return self.view.render("")

    def store(self):
        # TODO: check if can create appointment
        services = self.request.user().account.services.filter(
            lambda service: service.id in self.request.input("services")
        )
        price = services.pluck("price").sum()
        appointment = Appointment.create(
            start_time=self.request.input("start_time"),
            finish_time=self.request.input("finish_time"),
            client_id=self.request.input("client_id"),
            client_name=self.request.input("client_name"),
            client_email=self.request.input("client_email"),
            client_phone=self.request.input("client_phone"),
            price=price,
            account_id=self.request.user().account.id,
            staff_id=self.request.input("staff"),
        ).fresh()

        appointment.save_many("services", services)

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
