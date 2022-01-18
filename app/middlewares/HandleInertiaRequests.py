import json

from masonite.facades import Session
from masonite.inertia import InertiaMiddleware


class HandleInertiaRequests(InertiaMiddleware):
    def get_success(self, session):
        if not isinstance(session.get("success"), str) and session.has("success"):
            return session.get("success").json()
        else:
            return {}

    def share(self, request):
        session = request.app.make("session")
        success = self.get_success(session)
        return {"success": success}
