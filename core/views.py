from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from chat_app.models import User
from core.forms import RegistrationForm, UserAuthenticationForm


class RegistrationView(FormView):
    template_name = "core/registration.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("core_app:registration_success")

    def form_valid(self, form):
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        gender = form.cleaned_data["gender"]
        date_of_birth = form.cleaned_data["date_of_birth"]
        contact_number = form.cleaned_data["contact_number"]

        # Hash the password
        hashed_password = make_password(password)

        # create a new user object and save it
        user = User(
            name=name,
            email=email,
            password=hashed_password,
            gender=gender,
            date_of_birth=date_of_birth,
            contact_number=contact_number,
        )
        user.save()
        return super().form_valid(form)


class RegistrationSuccessView(TemplateView):
    template_name = "chat_app/home.html"


class UserLoginView(LoginView):
    template_name = "core/login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy("chat_app:room")
    form_class = UserAuthenticationForm


# Logout View
class UserLogoutView(LogoutView):
    next_page = reverse_lazy("chat_app:home")
