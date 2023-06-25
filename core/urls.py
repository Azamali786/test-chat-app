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
]
