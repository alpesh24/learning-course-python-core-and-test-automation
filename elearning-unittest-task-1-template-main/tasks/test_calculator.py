"""Docstring."""

import unittest
from tasks.calculator import Calculator


class TestCalculator(unittest.TestCase):
    """This class contains unit tests for the Calculator module."""

    def setUp(self):
        self.calculator = Calculator()

    def test_sum(self):
        """
        Test case description: This test checks sum of two numbers.
        """
        self.assertEqual(self.calculator.sum(2, 3), 5)
        self.assertEqual(self.calculator.sum(-1, 1), 0)
        self.assertEqual(self.calculator.sum(0, 0), 0)

    def test_multiply(self):
        """
        Test case description: This test checks multiplication of two numbers.
        """
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.multiply(-1, 1), -1)
        self.assertEqual(self.calculator.multiply(2, 0), 0)

    def test_subtract(self):
        """
        Test case description: This test checks substraction of two numbers.
        """
        self.assertEqual(self.calculator.subtract(3, 2), 1)
        self.assertEqual(self.calculator.subtract(-1, 1), -2)
        self.assertEqual(self.calculator.subtract(0, 0), 0)

    def test_divide(self):
        """
        Test case description: This test checks division of two numbers.
        """
        self.assertEqual(self.calculator.divide(6, 3), 2)
        self.assertEqual(self.calculator.divide(5, 2), 2.5)
        self.assertIsNone(self.calculator.divide(5, 0))

    def test_sqrt(self):
        """
        Test case description: This test checks square root of number.
        """
        self.assertAlmostEqual(self.calculator.sqrt(4), 2.0)
        self.assertAlmostEqual(self.calculator.sqrt(9), 3.0)
        self.assertAlmostEqual(self.calculator.sqrt(2), 1.41, places=2)

    def test_pi(self):
        """
        Test case description: This test checks radian value for given angle.
        """
        self.assertAlmostEqual(self.calculator.pi(90), 1.57, places=2)
        self.assertAlmostEqual(self.calculator.pi(180), 3.14, places=2)
        self.assertAlmostEqual(self.calculator.pi(45), 0.79, places=2)


if __name__ == "__main__":
    unittest.main()
