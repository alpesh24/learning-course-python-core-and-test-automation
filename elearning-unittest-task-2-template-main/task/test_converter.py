"""Docstring."""

import unittest
from unittest.mock import patch
from task.converter import Converter


def mock_converter(_, celsius):
    return celsius * 9/5 + 32


class TestConverter(unittest.TestCase):

    def setUp(self):
        self.converter = Converter()

    @patch("task.converter.Converter.convert_celsius_to_fahrenheit", side_effect=mock_converter)
    def test_converter(self, mock_converter):
        result  = self.converter.convert_celsius_to_fahrenheit(0)
        self.assertEqual(result, 32)


if __name__ == "__main__":
    unittest.main()
