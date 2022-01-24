import unittest
import Library_Mock.website1 as web1
from unittest.mock import patch


class TestWebOne(unittest.TestCase):

    def test_poem_work(self):
        check_list = ['common@example.com', 'commoner@example.com', 'commonest@example.com']
        result_list = ['hello common', 'hello commoner', 'hello commonest']
        for check, result in zip(check_list, result_list):
            with patch('Library_Mock.web_data.data_to_send', return_value=check):
                self.assertEqual(web1.user_id(), result)

    def test_poem_work2(self):
        check_list = ['common@example.com', 'commoner@example.com', 'commonest@example.com']
        result_list = ['hello common', 'hello commoner', 'hello commonest']

        with patch('Library_Mock.web_data.data_to_send', side_effect=check_list):
            for result in result_list:
                self.assertEqual(web1.user_id(), result)

    def test_poem_value_error(self):
        check_list = ['S|<ape@example.com', 'monkey@@example.com', '$tark@example.com']
        for check in check_list:
            with patch('Library_Mock.web_data.data_to_send', return_value=check):
                with self.assertRaises(ValueError):
                    web1.user_id()

    def test_poem_type_error(self):
        check_list = [{'set@example.com'}, ['list@example.com'], 2023]
        for check in check_list:
            with patch('Library_Mock.web_data.data_to_send', return_value=check):
                with self.assertRaises(TypeError):
                    web1.user_id()


if __name__ == '__main__':
    unittest.main()
