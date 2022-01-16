from app.models.Service import Service
from app.models.Staff import Staff
from masonite.controllers import Controller
from masonite.facades import Request, Response, Session
from masonite.inertia import Inertia
from masonite.validation import Validator


class StaffsController(Controller):
    def __init__(
        self,
        view: Inertia,
        validate: Validator,
    ):
        self.view = view
        self.request = Request
        self.response = Response
        self.validate = validate
        self.session = Session

    def index(self):
        staffs = Staff.all()
        services = Service.all()
        return self.view.render(
            "Staff/index", {"staffs": staffs.serialize(), "services": services.serialize()}
        )

    def create(self):
        services = Service.all()
        return self.view.render("Staff/create", {"services": services.serialize()})

    def store(self):
        errors = self.request.validate(
            self.validate.required(["email", "name", "phone"]), self.validate.email("email")
        )

        if errors:
            self.session.flash("errors", errors)
            return self.response.redirect(name="staff.create").with_errors(errors).with_input()
        """ self.request.session.flash("errors", "Preencha os campos")
        return self.response.status(404) """

        Staff.create(**self.request.only("name", "email", "phone"))

        return self.response.back().with_success("Membro criado com sucesso.")

    def show(self):
        staff = Staff.find(self.request.param("staff"))
        return self.view.render("Staff/details", {"staff": staff.serialize()})

    def edit(self):
        staff = Staff.find(self.request.param("Staff_id"))
        services = Service.all()
        return self.view.render(
            "Staff/edit", {"staff": staff.serialize(), "services": services.serialize()}
        )

    def update(self):
        errors = self.request.validate(
            self.validate.required(["email", "name", "phone"]),
            self.validate.email("email"),
        )

        if errors:
            return self.response.redirect(name="staff.create").with_errors(errors).with_input()

        staff = Staff.find(self.request.param("Staff_id"))

        staff.update(**self.request.only("email", "name", "phone"))

        self.session.flash("success", "Membro criado com sucesso.")
        return self.response.redirect(name="staff.index")

    def destroy(self):
        staff = Staff.find(self.request.param("staff"))
        staff.delete()

        self.session.flash("success", "Membro apagado com sucesso.")
        return self.response.redirect(name="staff.index")
