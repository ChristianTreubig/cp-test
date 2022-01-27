from django.shortcuts import redirect
from django.conf import settings


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response
        self._login_url = settings.LOGIN_URL
        self._open_urls = [self._login_url] + settings.OPEN_URLS

    def __call__(self, request):
        if not request.user.is_authenticated and not request.path_info in self._open_urls:
            return redirect(self._login_url+'?next='+request.path)

        return self._get_response(request)
