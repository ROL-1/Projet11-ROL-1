"""Tests file for api_requests.py."""

from django.test import TestCase

from product.offapi.charmax import Charmax


class TestCharmax(TestCase):
    """Test for class : Charmax."""

    def test_characters_max_return_dict_with_max_characters_values_for_fields(
        self,
    ):
        """
        When database is request by characters_max() function, it returns a dict with
        maximums characters alloweds for a list fields.
        """
        assert Charmax.characters_max() == {
            "generic_name_fr": 100,
            "product_name_fr": 100,
            "url": 200,
            "image_url": 200,
            "categories": 75,
            "brands": 75,
        }

