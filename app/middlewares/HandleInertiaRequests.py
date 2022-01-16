import json

from masonite.facades import Session
from masonite.inertia import InertiaMiddleware


class HandleInertiaRequests(InertiaMiddleware):
    def get_success(self, session):
        if not isinstance(session.get("success"), str) and session.has("success"):
            return session.get("success").json()
        else:
            return {}

    def get_errors(self, session):
        if not isinstance(session.get("errors"), str) and session.has("errors"):
            return session.get("errors").json()
        else:
            return {}

    def share(self, request):
        session = request.app.make("session")
        errors = self.get_errors(session)
        success = self.get_success(session)
        return {"errors": errors, "success": success}
