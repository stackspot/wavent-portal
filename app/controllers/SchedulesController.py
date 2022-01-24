from app.models.Schedule import Schedule
from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from masonite.sessions import Session


class SchedulesController(Controller):
    def __init__(self, request: Request, response: Response, session: Session):
        self.request = request
        self.response = response
        self.session = session

    def index(self):
        return self.response.json({"schedules": self.request.user().account.schedules.serialize()})

    def create(self):
        pass

    def store(self):

        schedules = self.request.only("schedules")

        # TODO: not working
        try:
            if self.request.user().account.schedules:
                Schedule.where("account_id", self.request.user().account.id).delete()
            Schedule.bulk_create(schedules["schedules"])
        except Exception as e:
            return self.response.redirect(name="settings").with_errors(e)

        return self.response.redirect(name="settings").with_success("Horários criado com sucesso!")

    def show(self):
        pass

    def edit(self):
        pass

    def update(self):
        schedules = self.request.only("schedules")
        for schedule in schedules["schedules"]:
            print(schedule)
            horario = Schedule.find(schedule["id"])
            horario.update(
                {
                    "name": schedule["name"],
                    "start_time": schedule["start_time"],
                    "finish_time": schedule["finish_time"],
                    "is_working": schedule["is_working"],
                }
            )

        self.session.flash("success", "Horário Atualizado.")
        return self.response.json("Horário atualizado")

    def destroy(self):
        schedule = Schedule.find(self.request.param("schedule"))

        schedule.delete()

        self.session.flash("success", "Horário Removido.")
        return self.response.redirect(name="users.index")
