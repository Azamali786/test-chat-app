from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import (
    EmailValidator,
    MaxLengthValidator,
    MinLengthValidator,
)
from django.forms import DateInput
from django.utils import timezone

from chat_app.models import User


class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(validators=[EmailValidator()])
    password = forms.CharField(
        widget=forms.PasswordInput(),
        validators=[MinLengthValidator(6), MaxLengthValidator(10)],
    )
    date_of_birth = forms.DateField(
        widget=DateInput(attrs={"placeholder": "YYYY-MM-DD"})
    )
    contact_number = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "+917974007074"})
    )

    class Meta:
        model = User
        fields = (
            "name",
            "email",
            "password",
            "gender",
            "date_of_birth",
            "contact_number",
        )

    def clean_dob(self):
        date_of_birth = self.cleaned_data["date_of_birth"]
        if date_of_birth > timezone.localdate():
            raise ValidationError("Future date not allowed.")
        return date_of_birth
