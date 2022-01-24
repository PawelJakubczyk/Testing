import unittest
from unittest.mock import patch
from Library.employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """classmethod will run before all test begin"""
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        """classmethod will run after all test end"""
        print('tearDownClass')

    def setUp(self):
        """function will run before every single test"""
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self):
        """function will run after every single test"""
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    # Mocking #
    # def test_monthly_schedule(self):
    #     # We want to Mock request.get from employee module. We must Mock this object where they are actually used
    #     with patch('employee.request.get') as mocked_get:
    #         mocked_get.return_value.ok = True
    #         mocked_get.return_value.text = 'Success'
    #         schedule = self.emp_1.monthly_schedule('May')
    #         mocked_get.assert_called_with('http://company.com/Schafer/May')
    #         self.assertEqual(schedule, 'Success')
    #
    #         mocked_get.return_value.ok = False
    #         schedule = self.emp_2.monthly_schedule('Jube')
    #         mocked_get.assert_called_with('http://company.com/Smith/June')
    #         self.assertEqual(schedule, 'Bad Response!')

    # ++++++++ monthly_schedule function from employee.py ++++++++
    # def monthly_schedule(self, month):
    #     response = requests.get(f'http://company.com/{self.last}/{month}')
    #     if response.ok:
    #         return response.text
    #     else:
    #         return 'Bad Response!'


if __name__ == '__main__':
    unittest.main()
# $ python test_employee.py
