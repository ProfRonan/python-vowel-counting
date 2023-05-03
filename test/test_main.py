"""Esse arquivo testa o arquivo example_module.py"""

import unittest  # para criar o caso de teste
from main import count_vowels


class TestMain(unittest.TestCase):
    """Classe para testar o main.py"""

    def test_count_vowels_empty_string(self):
        """Tests count_vowels with an empty string."""
        self.assertEqual(count_vowels(""), 0)

    def test_count_vowels_no_vowels(self):
        """Tests count_vowels with a string that contains no vowels."""
        self.assertEqual(count_vowels("xyz"), 0)

    def test_count_vowels_all_vowels(self):
        """Tests count_vowels with a string that contains all vowels."""
        self.assertEqual(count_vowels("aeiou"), 5)

    def test_count_vowels_mixed_case(self):
        """Tests count_vowels with a string that contains mixed case letters."""
        self.assertEqual(count_vowels("AbCdeFG"), 2)

    def test_count_vowels_with_numbers(self):
        """Tests count_vowels with a string that contains numbers."""
        self.assertEqual(count_vowels("hello123"), 2)

    def test_count_vowels_with_special_characters(self):
        """Tests count_vowels with a string that contains special characters."""
        self.assertEqual(count_vowels("hello!@#"), 2)
