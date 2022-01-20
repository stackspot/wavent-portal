"""A WelcomeController Module."""
from masonite.controllers import Controller
from masonite.inertia import Inertia
from masonite.request import Request
from masonite.views import View


class WelcomeController(Controller):
    """WelcomeController Controller Class."""

    def show(self, view: Inertia, request: Request):
        return view.render("welcome", {"user_account": request.user().account.serialize()})
