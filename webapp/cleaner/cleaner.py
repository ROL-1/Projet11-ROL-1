"""Cleaner file."""

from string import punctuation

import unidecode


class Cleaner:
    """Clean a string. Return a list.

    In : user's query (string)
    Act : Change the sentence in lowercase.
            Remove punctuation.
            Remove accentuation.
    Out : make query_cleaned (list) accessible for main.py
    """

    def __init__(self, query):
        """Launch function clean."""
        self.question_send = query
        self.query_cleaned = self._split()

    @property
    def _uncapitalized(self):
        """Uncapitalize string."""
        uncapitalized = self.question_send.lower()
        return uncapitalized

    @property
    def _no_punctuation(self):
        """Remove puncutation."""
        no_punctuation = "".join(
            [i if i not in punctuation else " " for i in self._uncapitalized]
        )
        return no_punctuation

    @property
    def _no_accentuation(self):
        """Remove accentuation."""
        no_accentuation = unidecode.unidecode(self._no_punctuation)
        return no_accentuation

    def _split(self):
        query_cleaned = self._no_accentuation.split()
        return query_cleaned
