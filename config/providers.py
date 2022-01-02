from masonite.inertia import InertiaProvider
from masonite.js_routes import JSRoutesProvider
from masonite.notification.providers import NotificationProvider
from masonite.providers import (
    AuthenticationProvider,
    AuthorizationProvider,
    BroadcastProvider,
    CacheProvider,
    EventProvider,
    ExceptionProvider,
    FrameworkProvider,
    HashServiceProvider,
    HelpersProvider,
    MailProvider,
    ORMProvider,
    QueueProvider,
    RouteProvider,
    SessionProvider,
    StorageProvider,
    ViewProvider,
    WhitenoiseProvider,
)
from masonite.scheduling.providers import ScheduleProvider
from masonite.validation.providers import ValidationProvider

PROVIDERS = [
    FrameworkProvider,
    HelpersProvider,
    RouteProvider,
    ViewProvider,
    WhitenoiseProvider,
    ExceptionProvider,
    MailProvider,
    NotificationProvider,
    SessionProvider,
    CacheProvider,
    QueueProvider,
    ScheduleProvider,
    EventProvider,
    StorageProvider,
    BroadcastProvider,
    HashServiceProvider,
    AuthenticationProvider,
    ValidationProvider,
    AuthorizationProvider,
    ORMProvider,
    # third party packages
    InertiaProvider,
    # JSRoutesProvider
]
