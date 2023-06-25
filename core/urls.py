from django.urls import path

from core import views

app_name = "core_app"

urlpatterns = [
    path("register/", views.RegistrationView.as_view(), name="registration"),
    path(
        "registration_success/",
        views.RegistrationSuccessView.as_view(),
        name="registration_success",
    ),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
]
