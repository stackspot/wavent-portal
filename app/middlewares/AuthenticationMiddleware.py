from unicodedata import name

from masonite.middleware import Middleware


class AuthenticationMiddleware(Middleware):
    def before(self, request, response):
        if request.user() == None:
            return response.redirect(name="login")
        return request

    def after(self, request, response):

        return request
