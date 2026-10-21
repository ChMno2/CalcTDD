import unittest
from calculator import Calculator  # The class we are going to implement

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)  # Expect 2 + 3 = 5

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)  # negative results are allowed

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)
        self.assertEqual(self.calc.multiply(-4, 3), -12)
        self.assertEqual(self.calc.multiply(7, 0), 0)

    def test_divide_returns_float(self):
        self.assertEqual(self.calc.divide(6, 3), 2.0)
        self.assertEqual(self.calc.divide(7, 2), 3.5)  # true division, not 3
        self.assertIsInstance(self.calc.divide(6, 3), float)

    def test_divide_by_zero_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

if __name__ == "__main__":
    unittest.main()