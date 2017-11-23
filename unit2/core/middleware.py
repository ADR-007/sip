from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect


class SelectLanguageMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(
            self,
            request: WSGIRequest
    ):
        if request.get_signed_cookie('lang', None):
            return self.get_response(request)  # type: WSGIRequest
        else:
            return redirect('/lang')
