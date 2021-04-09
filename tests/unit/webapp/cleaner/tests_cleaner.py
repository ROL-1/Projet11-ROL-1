"""Tests file for cleaner.py."""

from django.test import TestCase

from webapp.cleaner.cleaner import Cleaner


class TestCleaner(TestCase):
    """Test for class : Cleaner."""

    def test_Cleaner(self):
        """Cleaner.py main test."""
        question_send = "Salut Ô GrandPy, seigneur des adresses ! \
            Ca a été ta soirée ?"
        assert Cleaner(question_send).query_cleaned == [
            "salut",
            "o",
            "grandpy",
            "seigneur",
            "des",
            "adresses",
            "ca",
            "a",
            "ete",
            "ta",
            "soiree",
        ]

    def test_uncapitalized(self):
        """Cleaner.py function _uncapitalized_string test."""
        question_send = "TesT tHIs"
        assert Cleaner(question_send)._uncapitalized == "test this"

    def test_no_punctuation(self):
        """Cleaner.py function _no_punctuation test."""
        question_send = "TesT !#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ tHIs"
        assert (
            Cleaner(question_send)._no_punctuation
            == "test                                 this"
        )

    def test_no_accentuation(self):
        """Cleaner.py function _no_accentuation test."""
        question_send = "çÇáéíóúýÁÉÍÓÚÝàèìòùÀÈÌÒÙãõñäëïöüÿÄËÏÖÜÃÕÑâêîôûÂÊÎÔÛ"
        assert (
            Cleaner(question_send)._no_accentuation
            == "ccaeiouyaeiouyaeiouaeiouaonaeiouyaeiouaonaeiouaeiou"
        )

    def test_split(self):
        """Cleaner.py function _split test."""
        question_send = "Salut Ô GrandPy !"
        assert Cleaner(question_send).query_cleaned == [
            "salut",
            "o",
            "grandpy",
        ]
