"""Tests file for wsgi.py."""

from django.test import TestCase

from purbeurre.wsgi import application, get_wsgi_application, os


class TestWsgi(TestCase):
    """Test for class : wsgi.py."""

    def test_wsgi(self):
        """Test wsgi."""
        self.assertEqual(type(application), type(get_wsgi_application()))

    def test_environ(self):
        """Test environ."""
        self.assertTrue(
            os.environ.setdefault(
                "DJANGO_SETTINGS_MODULE", "purbeurre.settings"
            )
        )

