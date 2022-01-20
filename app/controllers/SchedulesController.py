from app.models.Schedule import Schedule
from masonite.controllers import Controller
from masonite.facades import Request, Response, Session
from masonite.views import View


class SchedulesController(Controller):
    def __init__(self):
        self.request = Request
        self.response = Response
        self.session = Session

    def index(self):
        return self.response.json({"schedules": self.request.user().account.schedules.serialize()})

    def create(self):
        pass

    def store(self):

        try:
            self.request.user().account.schedules.bulk_create(
                [self.request.all().only("start_time", "finish_time", "is_working")]
            )
        except Exception as e:
            return self.response.redirect(name="settings").with_errors("Erro ao criar Horários")

        return self.response.redirect(name="settings")

    def show(self):
        pass

    def edit(self):
        pass

    def update(self):
        schedule = Schedule.find(self.request.param("schedule"))

        schedule.update({**self.request.only("start_time", "finish_time", "is_working")})

        self.session.flash("success", "Horário Atualizado.")
        return self.request.redirect("users.index")

    def destroy(self):
        schedule = Schedule.find(self.request.param("schedule"))

        schedule.delete()

        self.session.flash("success", "Horário Removido.")
        return self.request.redirect("users.index")
