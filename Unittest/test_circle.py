import unittest
from Library import circle
from math import pi


class TestCircle(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(circle.circle_area(1), 3.14, places=1)
        self.assertAlmostEqual(circle.circle_area(2), 12.56, places=1)
        self.assertAlmostEqual(circle.circle_area(2.3), 16.61, places=1)
        self.assertAlmostEqual(circle.circle_area(pi), 31.00, places=1)

    def test_circle_value(self):
        self.assertRaises(ValueError, circle.circle_area, -10)
        self.assertRaises(ValueError, circle.circle_area, -2)
        self.assertRaises(ValueError, circle.circle_area, -6)

    def test_circle_type(self):
        self.assertRaises(ValueError, circle.circle_area, [])
        self.assertRaises(ValueError, circle.circle_area, 'snow')
        self.assertRaises(ValueError, circle.circle_area, range(4))


if __name__ == '__main__':
    unittest.main()


