from django.urls import path
from allauth.account import views


app_name = "login"
urlpatterns = [
    path("accounts/login/", views.LoginView .as_view(), name="account_login"),
    path("accounts/signup/", views.SignupView .as_view(), name="account_signup"),
    path("accounts/logout/", views.LogoutView .as_view(), name="account_logout"),
    path("accounts/password/set/", views.PasswordSetView.as_view(), name="account_set_password"),
    path("accounts/password/change/", views.PasswordChangeView.as_view(), name="account_change_password"),
    path("accounts/password/reset/", views.PasswordResetView.as_view(), name="account_reset_password"),
    path("accounts/email/", views.EmailView.as_view(), name="account_email"),
]