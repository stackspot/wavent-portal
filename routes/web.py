from masonite.authentication import Auth
from masonite.routes import Route

from .controllers_routes import (
    ACCOUNT_ROUTES,
    APPOINTMENT_ROUTES,
    CLIENT_ROUTES,
    PROVIDER_ROUTES,
    SCHEDULE_ROUTES,
    SERVICE_ROUTES,
    STAFF_ROUTES,
    USER_ROUTES,
)

ROUTES = [
    Route.group(
        [
            Route.get("/", "WelcomeController@show").name("dashboard"),
            Route.group(
                USER_ROUTES,
                prefix="/utilizadores",
                name="users.",
            ),
            Route.group(
                STAFF_ROUTES,
                prefix="/equipa",
                name="staff.",
            ),
            Route.group(
                CLIENT_ROUTES,
                prefix="/cliente",
                name="client.",
            ),
            Route.group(
                ACCOUNT_ROUTES,
                prefix="/conta",
                name="account.",
            ),
            Route.group(
                PROVIDER_ROUTES,
                prefix="/empresa",
                name="provider.",
            ),
            Route.group(
                SCHEDULE_ROUTES,
                prefix="/horario",
                name="schedule.",
            ),
            Route.group(
                APPOINTMENT_ROUTES,
                prefix="/calendario",
                name="appointment.",
            ),
            Route.group(
                SERVICE_ROUTES,
                prefix="/servicos",
                name="service.",
            ),
            Route.get("/definicao", "SettingsController@index").name("settings"),
        ],
        prefix="/admin",
    ),
]

ROUTES += Auth.routes()
