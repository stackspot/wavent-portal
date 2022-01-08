import json

from masonite.facades import Session
from masonite.inertia import InertiaMiddleware


class HandleInertiaRequests(InertiaMiddleware):
    """def get_messages(self, session):
        return {
            "success": (session.get("success") or ""),
            "error": (session.get("error") or ""),
            "danger": (session.get("danger") or ""),
            "warning": (session.get("warning") or ""),
            "info": (session.get("info") or ""),
        }

    def get_errors(self, session):
        errors = json.dumps(session.get("errors")) if session.has("errors") else {}
        print(errors)
        return str(errors)

    def share(self, request):
        session = request.app.make("session")
        return {
            "errors": self.get_errors(session),
            "messages": self.get_messages(session),
        }"""
