from masonite.routes import Route

USER_ROUTES = [
    Route.get("", "UsersController@index").name("index"),
    Route.get("/novo", "UsersController@create").name("create"),
    Route.post("", "UsersController@store").name("store"),
    Route.get("/@user_id", "UsersController@edit").name("show"),
    Route.put("/@user_id", "UsersController@update").name("update"),
    Route.delete("/@user_id", "UsersController@delete").name("destroy"),
    # Route.post("/@user_id/settings", "SettingsController@user_settings").name("user.settings"),
]

ACCOUNT_ROUTES = [
    Route.get("", "AccountsController@index").name("index"),
    Route.post("/store", "AccountsController@store").name("store"),
    Route.get("/@account_id/profile", "AccountsController@edit").name("profile"),
    Route.put("/@account_id/update", "AccountsController@update").name("update"),
    Route.delete("/@account_id/destroy", "AccountsController@delete").name("destroy"),
    Route.get("/settings", "SettingsController@account_settings").name("account.settings"),
]

APPOINTMENT_ROUTES = [
    Route.get("", "AppointmentsController@index").name("index"),
    Route.post("/create", "AppointmentsController@store").name("store"),
    Route.get("/@appointment_id/edit", "AppointmentsController@edit").name("edit"),
    Route.put("/@appointment_id/update", "AppointmentsController@update").name("update"),
    Route.delete("/@appointment_id/delete", "AppointmentsController@delete").name("delete"),
    Route.get("/settings", "SettingsController@appointment_settings").name("appointment.settings"),
]

SCHEDULE_ROUTES = [
    Route.get("", "SchedulesController@show").name("index"),
    Route.post("", "SchedulesController@store").name("store"),
    Route.get("/@schedule_id/edit", "SchedulesController@edit").name("edit"),
    Route.put("/@schedule_id", "SchedulesController@update").name("update"),
]

SERVICE_ROUTES = [
    Route.get("", "ServicesController@index").name("index"),
    Route.get("/novo", "ServicesController@create").name("create"),
    Route.post("", "ServicesController@store").name("store"),
    Route.get("/@service_id/editar", "ServicesController@edit").name("edit"),
    Route.post("/@service_id", "ServicesController@update").name("update"),
    Route.delete("/@service_id", "ServicesController@delete").name("delete"),
]
CLIENT_ROUTES = [
    Route.get("", "ClientsController@index").name("index"),
    Route.get("/novo", "ClientsController@create").name("create"),
    Route.post("", "ClientsController@store").name("store"),
    Route.get("/@service_id", "ClientsController@show").name("show"),
    Route.post("/@service_id", "ClientsController@update").name("update"),
    Route.delete("/@service_id/destroy", "ClientsController@delete").name("delete"),
]
