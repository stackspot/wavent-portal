from masonite.authentication import Auth
from masonite.routes import Route

ROUTES = [
    Route.get("/", "WelcomeController@show"),
]

ROUTES += Auth.routes()
