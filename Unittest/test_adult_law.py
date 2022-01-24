import unittest
from Library import adult_law as id


class TestAdultLaws(unittest.TestCase):

    def setUp(self):
        self.citizen = id.Citizen(0, False)

    def tearDown(self):
        del self.citizen

    def set_citizen(self, new_age: (int or float), new_criminal_record: bool = False):
        self.citizen.age = new_age
        self.citizen.criminal_record = new_criminal_record
        return self.citizen

    def test_already_adult(self):
        self.assertTrue(self.set_citizen(54).is_adult())
        self.assertTrue(self.set_citizen(19).is_adult())

    def test_not_yet_adult(self):
        self.assertFalse(self.set_citizen(17).is_adult())
        self.assertFalse(self.set_citizen(4).is_adult())

    def test_can_buy_soft_alcohol(self):
        self.assertTrue(self.set_citizen(16).law_to_buy_alcohol(4))
        self.assertTrue(self.set_citizen(43).law_to_buy_alcohol(12))
        self.assertTrue(self.set_citizen(18).law_to_buy_alcohol(7))

    def test_can_buy_strong_alcohol(self):
        self.assertTrue(self.set_citizen(18).law_to_buy_alcohol(42))
        self.assertTrue(self.set_citizen(32).law_to_buy_alcohol(50))
        self.assertTrue(self.set_citizen(101).law_to_buy_alcohol(22))

    def test_can_not_buy_alcohol(self):
        self.assertFalse(self.set_citizen(2).law_to_buy_alcohol(2))
        self.assertFalse(self.set_citizen(8).law_to_buy_alcohol(4))
        self.assertFalse(self.set_citizen(15).law_to_buy_alcohol(20))
        self.assertFalse(self.set_citizen(9).law_to_buy_alcohol(40))

    def test_can_buy_weapons(self):
        self.assertTrue(self.set_citizen(32, False).law_to_buy_weapon())
        self.assertTrue(self.set_citizen(23).law_to_buy_weapon())

    def test_can_not_buy_weapons(self):
        self.assertFalse(self.set_citizen(23, True).law_to_buy_weapon())
        self.assertFalse(self.set_citizen(14, False).law_to_buy_weapon())
        self.assertFalse(self.set_citizen(20, True).law_to_buy_weapon())

    def test_alcohol_with_percent_do_not_exist(self):
        with self.assertRaises(ValueError):
            self.assertTrue(self.set_citizen(55).law_to_buy_alcohol(0))
            self.assertTrue(self.set_citizen(13).law_to_buy_alcohol(1200))
            self.assertTrue(self.set_citizen(21).law_to_buy_alcohol(-7))
            self.assertFalse(self.set_citizen(17).law_to_buy_alcohol(101))

    def test_wrong_alcohol_data_types(self):
        with self.assertRaises(TypeError):
            self.assertTrue(self.set_citizen(24).law_to_buy_alcohol(range(7)))
            self.assertFalse(self.set_citizen(30).law_to_buy_alcohol(20j))
            self.assertFalse(self.set_citizen(13).law_to_buy_alcohol([40]))
            self.assertTrue(self.set_citizen(15).law_to_buy_alcohol({-7}))
            self.assertFalse(self.set_citizen(19).law_to_buy_alcohol('101'))

    def test_wrong_criminal_record_data_type(self):
        with self.assertRaises(TypeError):
            self.set_citizen(55, []).law_to_buy_weapon()
            self.set_citizen(55, 16).law_to_buy_alcohol()
            self.set_citizen(55, 5j).law_to_buy_alcohol()

    def test_do_not_born_yet(self):
        with self.assertRaises(ValueError):
            self.set_citizen(-4).is_adult()
            self.set_citizen(-7).is_adult()
            self.set_citizen(-00.1).vote_law()
            self.set_citizen(-5).vote_law()
            self.set_citizen(-7).law_to_buy_alcohol(alcohol_percent=5.5)
            self.set_citizen(-11).law_to_buy_alcohol(alcohol_percent=40)
            self.set_citizen(-8).law_to_buy_weapon()
            self.set_citizen(-14).law_to_buy_weapon()

    def test_wrong_age_data_type(self):
        with self.assertRaises(ValueError):
            self.set_citizen('24').is_adult()
            self.set_citizen(range(5)).is_adult()
            self.set_citizen(print('hmm')).vote_law()
            self.set_citizen(77j).vote_law()
            self.set_citizen({}).law_to_buy_alcohol(alcohol_percent=5.5)
            self.set_citizen({'DA': 'Denmark'}).law_to_buy_alcohol(alcohol_percent=40)
            self.set_citizen(7j).law_to_buy_weapon()
            self.set_citizen(True).law_to_buy_weapon()
            self.set_citizen(range()).law_to_buy_alcohol(alcohol_percent='5.5')
            self.set_citizen([]).law_to_buy_alcohol(alcohol_percent=[40])
            self.set_citizen([4, 6]).law_to_buy_weapon()
            self.set_citizen({}).law_to_buy_weapon()


if __name__ == '__main__':
    unittest.main()
