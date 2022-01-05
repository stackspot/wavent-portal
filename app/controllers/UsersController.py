from app.models.User import User
from masonite.controllers import Controller
from masonite.inertia import Inertia
from masonite.request import Request
from masonite.response import Response
from masonite.sessions import Session
from masonite.validation import Validator


class UsersController(Controller):
    def __init__(
        self,
        view: Inertia,
        request: Request,
        response: Response,
        validate: Validator,
        session: Session,
    ):
        self.view = view
        self.request = request
        self.response = response
        self.validate = validate
        self.session = session

    def index(self):
        users = User.all()
        return self.view.render("User/index", {"users": users.serialize()})

    def invite_members(self):
        # TODO: get the invite member email, then
        # TODO: get the account_id and create a token with it then
        # TODO: send the token to the member email
        pass

    def accept_invite_members(self):
        # TODO: get the email and id from the token in the request object
        # TODO: make the member as staff
        # TODO: user the email and id from the token, redirect the member to registration page to register with email and id as input parameters
        pass

    def create(self):
        return self.view.render("User/create")

    def store(self):
        errors = self.request.validate(
            self.validate.required(["email", "name", "phone", "is_provider", "is_staff"]),
            self.validate.email("email"),
            self.validate.truphy(["is_provider", "is_staff"]),
            self.validate.regex("phone", pattern=r"^(\+?351)?9\d\d{7}$"),
            self.validate.when(self.validate.exists("password")).then(
                self.validate.strong("password", length=8, special=1)
            ),
        )

        if errors:
            return self.response.redirect(name="users.create").with_errors(errors).with_input()

        # TODO: implement add user to DB

        User.create(**self.request.all())

        self.session.flash("success", "Utilizador criado com sucesso.")

        return self.response.redirect(name="users.index")

    def show(self):
        user = User.find(self.request.param("user_id"))
        return self.view.render("User/details", {"user": user.serialize()})

    def edit(self):
        user = User.find(self.request.param("user_id"))
        return self.view.render("User/edit", {"user": user.serialize()})

    def update(self):
        errors = self.request.validate(
            self.validate.required(["email", "name", "phone", "is_provider", "is_staff"]),
            self.validate.email("email"),
            self.validate.truphy(["is_provider", "is_staff"]),
            self.validate.regex("phone", pattern=r"^(\+?351)?9\d\d{7}$"),
            self.validate.when(self.validate.exists("password")).then(
                self.validate.strong("password", length=8, special=1)
            ),
        )

        if errors:
            return self.response.redirect(name="users.create").with_errors(errors).with_input()

        user = User.find(self.request.param("user_id"))

        user.update(**self.request.only("email", "name", "phone", "is_provider", "is_staff"))

        self.session.flash("success", "Utilizador criado com sucesso.")
        return self.response.redirect(name="users.index")

    def destroy(self):
        user = User.find(self.request.param("user_id"))
        user.delete()

        self.session.flash("success", "Utilizador apagado com sucesso.")
        return self.response.redirect(name="users.index")
