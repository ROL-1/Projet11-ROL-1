"""Tests forms.py for user app."""

from django.test import TestCase

from user.forms import CustomUserCreationForm


class TestCustomUserCreationForm(TestCase):
    """Test CustomUserCreationForm."""

    @classmethod
    def setUp(cls):
        """Create a unique form for all tests."""
        cls.form = CustomUserCreationForm()

    def test_CustomUserCreationForm_email_label(self):
        """Test if custom label is correctly named."""
        self.assertTrue(self.form.fields["email"].label == "Email")

    def test_CustomUserCreationForm_error_messages_exists_is_created(self):
        """Test if custom error message 'exists' is created."""
        self.assertTrue(self.form.fields["email"].error_messages["exists"])

    def test_CustomUserCreationForm_error_messages(self):
        """Test if custom error message 'exists' is correctly named."""
        self.assertTrue(
            self.form.fields["email"].error_messages["exists"]
            == "Email déjà existant."
        )

    def test_if_form_is_valid_with_corrects_inputs(self):
        """Test if form is valid with corrects inputs."""
        form = CustomUserCreationForm(
            data={
                "email": "newuser@email.com",
                "username": "newuser",
                "password1": "pwdCOMPLEX@123",
                "password2": "pwdCOMPLEX@123",
            }
        )
        self.assertTrue(form.is_valid())

    def test_if_form_is_not_valid_with_no_email_input(self):
        """Test if form is not valid with no email input."""
        form = CustomUserCreationForm(
            data={
                "email": "",
                "username": "newuser",
                "password1": "pwdCOMPLEX@123",
                "password2": "pwdCOMPLEX@123",
            }
        )
        self.assertFalse(form.is_valid())
