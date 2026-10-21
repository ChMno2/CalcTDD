import unittest
from calculator import Calculator  # The class we are going to implement

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)  # Expect 2 + 3 = 5

    def test_subtract(self):
        calc = Calculator()
        self.assertEqual(calc.subtract(5, 3), 2)
        self.assertEqual(calc.subtract(3, 5), -2)  # negative results are allowed

    def test_multiply(self):
        calc = Calculator()
        self.assertEqual(calc.multiply(4, 3), 12)
        self.assertEqual(calc.multiply(-4, 3), -12)
        self.assertEqual(calc.multiply(7, 0), 0)

    def test_divide_returns_float(self):
        calc = Calculator()
        self.assertEqual(calc.divide(6, 3), 2.0)
        self.assertEqual(calc.divide(7, 2), 3.5)  # true division, not 3
        self.assertIsInstance(calc.divide(6, 3), float)

if __name__ == "__main__":
    unittest.main()