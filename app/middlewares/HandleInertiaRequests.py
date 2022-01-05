from masonite.helpers import url
from masonite.inertia import InertiaMiddleware
from masonite.response import Response


class HandleInertiaRequests(InertiaMiddleware):
    def shared(self, request):
        def url_back():
            if (
                request.get_path() != url.route("login", absolute=False)
                and request.get_back_path() != ""
                and request.get_back_path() != request.get_path()
            ):
                return request.get_back_path()
            else:
                return "empty"

        return {"urlPrev": url_back}
