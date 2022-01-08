from masonite.routes import Route

USER_ROUTES = [
    Route.get("", "UsersController@index").name("index"),
    Route.get("/novo", "UsersController@create").name("create"),
    Route.post("", "UsersController@store").name("store"),
    Route.get("/@user", "UsersController@edit").name("show"),
    Route.put("/@user", "UsersController@update").name("update"),
    Route.delete("/@user", "UsersController@delete").name("destroy"),
    # Route.post("/@user/settings", "SettingsController@user_settings").name("settings"),
]

ACCOUNT_ROUTES = [
    Route.get("", "AccountsController@index").name("index"),
    Route.post("/store", "AccountsController@store").name("store"),
    Route.get("/@account", "AccountsController@edit").name("profile"),
    Route.put("/@account", "AccountsController@update").name("update"),
    Route.delete("/@account", "AccountsController@delete").name("destroy"),
    Route.get("/settings", "SettingsController@account_settings").name("settings"),
]

ORGANIZATION_ROUTES = [
    Route.get("", "OrganizationsController@index").name("index"),
    Route.post("", "OrganizationsController@store").name("store"),
    Route.get("/@organization", "OrganizationsController@edit").name("profile"),
    Route.put("/@organization", "OrganizationsController@update").name("update"),
    Route.delete("/@organization", "OrganizationsController@delete").name("destroy"),
    Route.get("/settings", "SettingsController@organization_settings").name("settings"),
]

APPOINTMENT_ROUTES = [
    Route.get("", "AppointmentsController@index").name("index"),
    Route.post("/create", "AppointmentsController@store").name("store"),
    Route.get("/@appointment/edit", "AppointmentsController@edit").name("edit"),
    Route.put("/@appointment", "AppointmentsController@update").name("update"),
    Route.delete("/@appointment", "AppointmentsController@delete").name("delete"),
    Route.get("/settings", "SettingsController@appointment_settings").name("settings"),
]

SCHEDULE_ROUTES = [
    Route.get("", "SchedulesController@show").name("index"),
    Route.post("", "SchedulesController@store").name("store"),
    Route.get("/@schedule/edit", "SchedulesController@edit").name("edit"),
    Route.put("/@schedule", "SchedulesController@update").name("update"),
]

SERVICE_ROUTES = [
    Route.get("", "ServicesController@index").name("index"),
    Route.get("/novo", "ServicesController@create").name("create"),
    Route.post("", "ServicesController@store").name("store"),
    Route.get("/@service/editar", "ServicesController@edit").name("edit"),
    Route.post("/@service", "ServicesController@update").name("update"),
    Route.delete("/@service", "ServicesController@delete").name("delete"),
]
CLIENT_ROUTES = [
    Route.get("", "ClientsController@index").name("index"),
    Route.get("/novo", "ClientsController@create").name("create"),
    Route.post("", "ClientsController@store").name("store"),
    Route.get("/@service", "ClientsController@show").name("show"),
    Route.post("/@service", "ClientsController@update").name("update"),
    Route.delete("/@service/destroy", "ClientsController@delete").name("delete"),
]
