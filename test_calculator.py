# https://github.com/Stella-Seitz/Lab-10-SS-BO/blob/main/test_calculator.py
from unittest import TestCase
from calculator import add, subtract, mul, div, logarithm, exp, hypotenuse, square_root


class TestCalculator(TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-5, -3), -2)
        self.assertEqual(subtract(0, 0), 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
        self.assertEqual(div(5, 10), 2)

    def test_multiply(self):
        self.assertEqual(mul(2, 5), 10)
        self.assertEqual(mul(2, -5), -10)
        self.assertEqual(mul(-2, -5), 10)
        self.assertEqual(mul(100, 5), 500)

    def test_divide(self):
        self.assertEqual(div(5, 10), 2)
        self.assertEqual(div(-5, 10), -2)
        self.assertEqual(div(5, -10), -2)
        self.assertEqual(div(-5, -10), 2)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError) as Error:
            logarithm(-1, 4)
            logarithm(1, -4)
            logarithm(0, 4)
            logarithm(1, 0)

    def test_hypotenuse(self):
        with self.assertRaises(ValueError) as Error:
            hypotenuse(-1, 4)
            hypotenuse(1, -4)
            hypotenuse(0, 4)
            hypotenuse(1, 0)

    def test_sqrt(self):
        with self.assertRaises(ValueError) as Error:
            square_root(-1)
            square_root(0)

    def test_logarithm(self):
        self.assertEqual(logarithm(10, 100), .5)
        self.assertEqual(logarithm(2, 2), 1)
        self.assertEqual(logarithm(4, 2), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 10)
        with self.assertRaises(ValueError):
            logarithm(0, 10)
        with self.assertRaises(ValueError):
            logarithm(-2, 10)
        with self.assertRaises(ValueError):
            logarithm(2, -10)

if __name__ == "__main__":
    unittest.main()