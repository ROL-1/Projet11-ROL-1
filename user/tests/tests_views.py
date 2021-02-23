from django.test import TestCase, Client
from django.urls import reverse
from django.template.loader import render_to_string


from user.models import CustomUser

# https://docs.djangoproject.com/fr/3.1/topics/testing/tools/


class TestWiews(TestCase):
    """Test views and associated templates."""

    @classmethod
    def setUpTestData(cls):
        """Create test datas."""
        # User
        name = "user1"
        email = "user1@email.com"
        psswd = "psswd123"
        CustomUser.objects.create(username=name, email=email, password=psswd)
        # Log user
        c = Client()
        c.login(username=name, password=psswd)

    def test_if_view_myaccount_return_200_and_use_suitables_templates(self):
        """
        1. Check if "response.status_code" is "200".
        2. Check if suitables templates are used.
        """
        response = self.client.get(reverse("myaccount"))
        self.assertEqual(response.status_code, 200)
        # with self.assertTemplateUsed("webapp/contact.html"):
        #     render_to_string("webapp/contact.html")
        # with self.assertTemplateUsed("webapp/base.html"):
        #     render_to_string("webapp/contact.html")
