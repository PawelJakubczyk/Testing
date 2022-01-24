import  unittest
from Library.triangle import get_triangle_field as field


class TestTriangle(unittest.TestCase):
    def test_triangle_get_field(self):
        self.assertEqual((field(5, 10)), 25)



# def get_triangle_field(base: (int or float), height: (int or float)) -> print(float):
#     field = base * height/2
#     print(field)
