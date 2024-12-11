from django.shortcuts import render
from django.views import View


class LoginRedirect(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        return render(request, "login_redirect.html", {"user": user})

class LogoutRedirect(View):
    def get(self, request, *args, **kwargs):
        return render(request, "logout_redirect.html")