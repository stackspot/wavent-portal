from masonite.authentication import Auth
from masonite.routes import Route

from .controllers_routes import (
    ACCOUNT_ROUTES,
    APPOINTMENT_ROUTES,
    CLIENT_ROUTES,
    SCHEDULE_ROUTES,
    SERVICE_ROUTES,
    USER_ROUTES,
)

ROUTES = [
    Route.get("/", "WelcomeController@show"),
    Route.group(
        [
            Route.group(
                USER_ROUTES,
                prefix="/equipa",
                name="users.",
            ),
            Route.group(
                CLIENT_ROUTES,
                prefix="/cliente",
                name="client.",
            ),
            Route.group(
                ACCOUNT_ROUTES,
                prefix="/account",
                name="account.",
            ),
            Route.group(
                SCHEDULE_ROUTES,
                prefix="/schedule",
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
        ],
        prefix="/admin",
    ),
]

ROUTES += Auth.routes()
