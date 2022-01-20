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

        account_slug = slugify(request.input("name"))
        account = Account.create({"name": request.input("name"), "slug": account_slug}).fresh()
        user = auth.register(
            {
                "name": request.input("name"),
                "email": request.input("email"),
                "password": request.input("password"),
                "phone": request.input("phone"),
                "account_id": account.id,
            }
        )
        if not user:
            return response.redirect(name="register")

        return response.redirect(name="dashboard")
