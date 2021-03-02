"""Tests file for api_requests.py."""

from django.test import TestCase

from product.offapi.api_requests import ApiRequests


class TestApiRequests(TestCase):
    """Test for class : ApiRequests."""

    @classmethod
    def setUpTestData(cls):
        """Create test datas."""
        cls.Fields_charmax = {
            "generic_name_fr": 100,
            "product_name_fr": 100,
            "url": 200,
            "image_url": 200,
            "categories": 75,
            "brands": 75,
        }

    # def test_api_request(self):
    #     """api_request() test."""
    #     category = "Pizza"
    #     results =

    #     question_send = "Salut Ô GrandPy, seigneur des adresses ! \
    #         Ca a été ta soirée ?"
    #     assert Cleaner(question_send).query_cleaned == [
    #         "salut",
    #         "o",
    #         "grandpy",
    #         "seigneur",
    #         "des",
    #         "adresses",
    #         "ca",
    #         "a",
    #         "ete",
    #         "ta",
    #         "soiree",
    #     ]

    # def test_uncapitalized(self):
    #     """Cleaner.py function _uncapitalized_string test."""
    #     question_send = "TesT tHIs"
    #     assert Cleaner(question_send)._uncapitalized == "test this"

    # def test_no_punctuation(self):
    #     """Cleaner.py function _no_punctuation test."""
    #     question_send = "TesT !#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ tHIs"
    #     assert (
    #         Cleaner(question_send)._no_punctuation
    #         == "test                                 this"
    #     )

    # def test_no_accentuation(self):
    #     """Cleaner.py function _no_accentuation test."""
    #     question_send = "çÇáéíóúýÁÉÍÓÚÝàèìòùÀÈÌÒÙãõñäëïöüÿÄËÏÖÜÃÕÑâêîôûÂÊÎÔÛ"
    #     assert (
    #         Cleaner(question_send)._no_accentuation
    #         == "ccaeiouyaeiouyaeiouaeiouaonaeiouyaeiouaonaeiouaeiou"
    #     )

    # def test_split(self):
    #     """Cleaner.py function _split test."""
    #     question_send = "Salut Ô GrandPy !"
    #     assert Cleaner(question_send).query_cleaned == [
    #         "salut",
    #         "o",
    #         "grandpy",
    #     ]
