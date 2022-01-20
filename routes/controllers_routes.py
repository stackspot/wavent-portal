from masonite.routes import Route

USER_ROUTES = [
    Route.get("", "UsersController@index").name("index"),
    Route.get("/novo", "UsersController@create").name("create"),
    Route.post("", "UsersController@store").name("store"),
    Route.get("/@user", "UsersController@edit").name("show"),
    Route.put("/@user", "UsersController@update").name("update"),
    Route.delete("/@user", "UsersController@destroy").name("destroy"),
    # Route.post("/@user/settings", "SettingsController@user_settings").name("settings"),
]

STAFF_ROUTES = [
    Route.get("", "StaffsController@index").name("index"),
    Route.get("/novo", "StaffsController@create").name("create"),
    Route.post("", "StaffsController@store").name("store"),
    Route.get("/@staff", "StaffsController@edit").name("edit"),
    Route.get("/@staff", "StaffsController@show").name("show"),
    Route.put("/@staff", "StaffsController@update").name("update"),
    Route.delete("/@staff", "StaffsController@destroy").name("destroy"),
    # Route.post("/@staff/settings", "SettingsController@staff_settings").name("settings"),
]

ACCOUNT_ROUTES = [
    Route.get("", "AccountsController@index").name("index"),
    Route.post("/store", "AccountsController@store").name("store"),
    Route.get("/@account", "AccountsController@edit").name("profile"),
    Route.put("/@account", "AccountsController@update").name("update"),
    Route.delete("/@account", "AccountsController@destroy").name("destroy"),
    Route.get("/settings", "SettingsController@account_settings").name("settings"),
]

PROVIDER_ROUTES = [
    Route.get("", "ProvidersController@index").name("index"),
    Route.post("", "ProvidersController@store").name("store"),
    Route.get("/@provider", "ProvidersController@edit").name("profile"),
    Route.put("/@provider", "ProvidersController@update").name("update"),
    Route.delete("/@provider", "ProvidersController@destroy").name("destroy"),
    Route.get("/settings", "SettingsController@provider_settings").name("settings"),
]

APPOINTMENT_ROUTES = [
    Route.get("", "AppointmentsController@index").name("index"),
    Route.post("/create", "AppointmentsController@store").name("store"),
    Route.get("/@appointment/edit", "AppointmentsController@edit").name("edit"),
    Route.put("/@appointment", "AppointmentsController@update").name("update"),
    Route.delete("/@appointment", "AppointmentsController@destroy").name("delete"),
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
    Route.delete("/@service", "ServicesController@destroy").name("delete"),
]
CLIENT_ROUTES = [
    Route.get("", "ClientsController@index").name("index"),
    Route.get("/novo", "ClientsController@create").name("create"),
    Route.post("", "ClientsController@store").name("store"),
    Route.get("/@client", "ClientsController@show").name("show"),
    Route.post("/@client", "ClientsController@update").name("update"),
    Route.delete("/@client/destroy", "ClientsController@destroy").name("delete"),
]
