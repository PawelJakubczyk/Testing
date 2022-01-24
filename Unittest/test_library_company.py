import unittest
import Library.company as lib


class TestCompanyFile(unittest.TestCase):
    def test_allow_country(self):
        country_test_list = ['DK', 'DE']
        for iso_code in country_test_list:
            country = lib.get_country(iso_code=iso_code)
            self.assertTrue(country[0])
            self.assertEqual(type(country[1]), dict)

    def test_disallow_country(self):
        country = lib.get_country(iso_code='DA')
        self.assertFalse(country[0])
        self.assertIsNone(country[1])

    def test_raise_country_TypeError(self):
        with self.assertRaises(TypeError):
            lib.get_country()
            lib.get_country(iso_code=12)

    def test_raise_country_ValueError(self):
        with self.assertRaises(ValueError):
            lib.get_country(iso_code='D')
            lib.get_country(iso_code='')
            lib.get_country(iso_code='Denmark')


if __name__ == '__main__':
    unittest.main()
