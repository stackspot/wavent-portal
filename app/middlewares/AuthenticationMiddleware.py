from masonite.middleware import Middleware


class AuthenticationMiddleware(Middleware):
    def before(self, request, response):
        if not request.user():
            return response.redirect(name="login")
        else:
            return response.redirect(request.get_path())
        return request

    def after(self, request, response):
        return request
