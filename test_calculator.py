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

    def test_modulo_result_has_sign_of_divisor(self):
        # Decision (user): Python/floor semantics, result takes the divisor's sign
        self.assertEqual(self.calc.modulo(7, 3), 1)
        self.assertEqual(self.calc.modulo(-7, 3), 2)
        self.assertEqual(self.calc.modulo(7, -3), -2)
        self.assertEqual(self.calc.modulo(-7, -3), -1)

    def test_modulo_by_zero_raises_value_error(self):
        # Decision (user): same contract as divide, ValueError instead of ZeroDivisionError
        with self.assertRaises(ValueError):
            self.calc.modulo(5, 0)

    def test_power_non_negative_exponent(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(-2, 3), -8)
        self.assertEqual(self.calc.power(5, 0), 1)
        # Decision (user): power(0, 0) is 1, following programming-language convention
        self.assertEqual(self.calc.power(0, 0), 1)

    def test_power_negative_exponent_returns_float(self):
        # Decision (user): negative exponent gives a float reciprocal
        self.assertEqual(self.calc.power(2, -1), 0.5)
        self.assertEqual(self.calc.power(2, -2), 0.25)
        self.assertIsInstance(self.calc.power(2, -1), float)
        # 0 to a negative power is 1/0, so it follows the ValueError contract of divide
        with self.assertRaises(ValueError):
            self.calc.power(0, -1)

if __name__ == "__main__":
    unittest.main()
