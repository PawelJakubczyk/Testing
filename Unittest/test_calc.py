import unittest
from Library import calc


# https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug


class TestCalc(unittest.TestCase):
    # All test function must start from test_
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 2), 1)
        self.assertEqual(calc.add(3, 5), 8)
        self.assertEqual(calc.add(-2, -3), -5)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 2), -3)
        self.assertEqual(calc.subtract(3, 5), -2)
        self.assertEqual(calc.subtract(-2, -3), 1)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 2), -2)
        self.assertEqual(calc.multiply(3, 5), 15)
        self.assertEqual(calc.multiply(-2, -3), 6)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 2), -0.5)
        self.assertEqual(calc.divide(-6, -3), 2)
        self.assertRaises(ValueError, calc.divide, 10, 0)
        with self.assertRaises(ValueError):
            calc.divide(-6, 0)


###################################
if __name__ == '__main__':
    unittest.main()
# Console:
# $ python test_calc.py
###################################
# Or
###################################
# Console:
# $ python -m unittest test_calc.py
###################################
# Result v
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.001s
#
# OK









