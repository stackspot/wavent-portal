from masonite.authentication import Auth
from masonite.controllers import Controller
from masonite.inertia import Inertia
from masonite.request import Request
from masonite.response import Response


class LoginController(Controller):
    def show(self, view: Inertia):
        return view.render("Auth/login")

    def store(self, request: Request, auth: Auth, response: Response):
        login = auth.attempt(request.input("email"), request.input("password"))

        if login:
            return response.redirect(name="dashboard")

        # Go back to login page
        return response.redirect(name="login").with_errors(["O email e/ou a palavra-passe está incorreto!"])

    def logout(self, auth: Auth, response: Response):
        auth.logout()
        return response.redirect(name="login")
