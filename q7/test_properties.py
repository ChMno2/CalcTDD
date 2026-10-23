import random
import unittest
from calculator import Calculator

SAMPLES = 500
SEED = 2026


class TestCalculatorProperties(unittest.TestCase):
    """Property-based and metamorphic tests: no expected value is hard-coded."""

    def setUp(self):
        self.calc = Calculator()
        self.rng = random.Random(SEED)

    def ints(self, lo=-10**6, hi=10**6):
        return self.rng.randint(lo, hi)

    def pairs(self, nonzero_b=False):
        for _ in range(SAMPLES):
            a, b = self.ints(), self.ints()
            if nonzero_b and b == 0:
                b = 1
            yield a, b

    def test_add_is_commutative(self):
        for a, b in self.pairs():
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.add(a, b), self.calc.add(b, a))

    def test_add_zero_is_identity(self):
        for a, _ in self.pairs():
            with self.subTest(a=a):
                self.assertEqual(self.calc.add(a, 0), a)

    def test_subtract_undoes_add(self):
        for a, b in self.pairs():
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.subtract(self.calc.add(a, b), b), a)

    def test_subtract_is_anticommutative(self):
        for a, b in self.pairs():
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.subtract(a, b), -self.calc.subtract(b, a))

    def test_multiply_is_commutative(self):
        for a, b in self.pairs():
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.multiply(a, b), self.calc.multiply(b, a))

    def test_multiply_distributes_over_add(self):
        # a * (b + 1) == a * b + a
        for a, b in self.pairs():
            with self.subTest(a=a, b=b):
                self.assertEqual(
                    self.calc.multiply(a, self.calc.add(b, 1)),
                    self.calc.add(self.calc.multiply(a, b), a),
                )

    def test_divide_undoes_multiply(self):
        for a, b in self.pairs(nonzero_b=True):
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.divide(self.calc.multiply(a, b), b), a)

    @unittest.expectedFailure
    def test_divide_undoes_multiply_beyond_2_53(self):
        # Known limitation of the Q1 decision that divide returns a float:
        # integers above 2**53 are not representable exactly as floats.
        for a, b in self.pairs(nonzero_b=True):
            a += 2**53
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.divide(self.calc.multiply(a, b), b), a)

    def test_divide_times_divisor_recovers_dividend(self):
        for a, b in self.pairs(nonzero_b=True):
            with self.subTest(a=a, b=b):
                self.assertAlmostEqual(
                    self.calc.multiply(self.calc.divide(a, b), b), a, delta=1e-6 * max(1, abs(a))
                )

    def test_divide_always_returns_float(self):
        for a, b in self.pairs(nonzero_b=True):
            with self.subTest(a=a, b=b):
                self.assertIsInstance(self.calc.divide(a, b), float)

    def test_divide_by_zero_always_raises_value_error(self):
        for a, _ in self.pairs():
            with self.subTest(a=a):
                with self.assertRaises(ValueError):
                    self.calc.divide(a, 0)


if __name__ == "__main__":
    unittest.main()
