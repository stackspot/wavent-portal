from masonite.controllers import Controller
from masonite.inertia import Inertia


class SettingsController(Controller):
    def __init__(self, view: Inertia):
        self.view = view

    def index(self):
        return self.view.render("Settings/index")

    def create(self):
        return self.view.render("")

    def store(self):
        return self.view.render("")

    def show(self):
        return self.view.render("")

    def edit(self):
        return self.view.render("")

    def update(self):
        return self.view.render("")

    def destroy(self):
        return self.view.render("")
