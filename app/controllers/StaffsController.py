import email

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
        return self.view.render(
            "Staff/index",
            {
                "staffs": self.request.user().account.staffs.serialize(),
            },
        )

    def create(self):
        return self.view.render(
            "Staff/create", {"services": self.request.user().account.services.serialize()}
        )

    def store(self):
        errors = self.request.validate(
            self.validate.required(["email", "name", "phone"]), self.validate.email("email")
        )

        if errors:
            self.session.flash("errors", errors)
            return self.response.redirect(name="staff.create").with_errors(errors).with_input()
        """ self.request.session.flash("errors", "Preencha os campos")
        return self.response.status(404) """

        Staff.create(
            name=self.request.input("name"),
            email=self.request.input("email"),
            phone=self.request.input("phone"),
            account_id=self.request.user().account.id,
        )

        return self.response.back().with_success("Membro criado com sucesso.")

    def show(self):
        staff = Staff.find(self.request.param("staff"))
        return self.view.render("Staff/details", {"staff": staff.serialize()})

    def edit(self):
        staff = Staff.find(self.request.param("staff"))
        services = Service.all()
        return self.view.render(
            "Staff/edit", {"staff": staff.serialize(), "services": services.serialize()}
        )

    def update(self):
        staff = Staff.find(self.request.param("staff"))

        if not staff:
            return self.response.back().with_errors("Membro não existe no sistema!")
        errors = self.request.validate(
            self.validate.required(["email", "name", "phone"]),
            self.validate.email("email"),
        )

        if errors:
            return self.response.redirect(name="staff.create").with_errors(errors).with_input()

        staff.update(**self.request.only("email", "name", "phone"))

        self.session.flash("success", "Membro criado com sucesso.")
        return self.response.redirect(name="staff.index")

    def destroy(self):
        staff = Staff.find(self.request.param("staff"))
        staff.delete()

        self.session.flash("success", "Membro apagado com sucesso.")
        return self.response.redirect(name="staff.index")
