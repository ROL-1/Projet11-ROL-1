"""Tests views for user app."""

from django.test import TestCase, Client
from django.urls import reverse
from django.template.loader import render_to_string


from user.models import CustomUser


class TestWiews(TestCase):
    """Test views and associated templates."""

    def test_if_view_myaccount_return_302_and_use_suitables_templates(self):
        """Test myaccount view.

        1. Check if "response.status_code" is "302".
        2. Check if suitables templates are used.
        """
        response = self.client.get(reverse("myaccount"))
        self.assertEqual(response.status_code, 302)
        with self.assertTemplateUsed(
            "user/myaccount.html"
        ), self.assertTemplateUsed("webapp/base.html"):
            render_to_string("user/myaccount.html")

    def test_if_view_signup_return_200_and_use_suitables_templates(self):
        """Test signup view.
        
        1. Check if "response.status_code" is "200".
        2. Check if suitables templates are used.
        """
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        with self.assertTemplateUsed(
            "registration/signup.html"
        ), self.assertTemplateUsed("webapp/base.html"):
            render_to_string("registration/signup.html")

