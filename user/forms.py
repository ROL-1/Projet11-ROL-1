"""forms for user app."""

from django.contrib.auth.forms import UserCreationForm
from user.models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):
    """Define a custom form for create a new user."""

    email = forms.EmailField(
        required=True,
        label="Email",
        error_messages={"exists": "Email déjà existant."},
    )

    class Meta(UserCreationForm.Meta):
        """Meta options for custom user form."""

        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("email",)
