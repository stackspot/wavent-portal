from app.models.Account import Account
from masonite.authentication import Auth
from masonite.controllers import Controller
from masonite.inertia import Inertia
from masonite.request import Request
from masonite.response import Response
from masonite.views import View
from slugify import slugify


class RegisterController(Controller):
    def show(self, view: Inertia):  # Show register page
        return view.render("Auth/register")

    def store(self, auth: Auth, request: Request, response: Response):  # store register user
        errors = request.validate(
            {
                "email": "required",
                "name": "required",
                "phone": "required",
                "password": "required|strong|confirmed",
            }
        )

        if errors:
            return response.back().with_errors(errors)

        user = auth.register(request.only("name", "email", "password", "phone"))
        if user:

            Account.create({"name": auth.user().name, "slug": slugify(auth.user().name)})
        if not user:
            return response.redirect("/register")

        return response.redirect(name="dashboard")
