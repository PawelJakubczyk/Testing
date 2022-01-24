import unittest
from unittest.mock import patch
import Library_Mock.poem as poem

# def poem_cuter():
#     text_to_cut = open('Library/poem.txt', 'r')
#     return text_to_cut


class TestPoem(unittest.TestCase):

    def test_poem(self):
        line_list = [0, 3, 5, 9]
        verse_list = ['Two roads diverged in a yellow wood,', 'And looked down one as far as I could',
                      '', 'Though as for that the passing there']

        with patch('Library_Mock.poem', return_value='Unittest_Mock.mock_poem'):
            for line, verse in zip(line_list, verse_list):
                self.assertEqual(poem.poem_cuter(line), verse)


# class TestWebOne(unittest.TestCase):
#
#     def test_poem_work(self):
#         check_list = ['common@example.com', 'commoner@example.com', 'commonest@example.com']
#         result_list = ['hello common', 'hello commoner', 'hello commonest']
#         for check, result in zip(check_list, result_list):
#             with patch('Library_Mock.web_data.data_to_send', return_value=check):
#                 self.assertEqual(web1.user_id(), result)
#
#     def test_poem_work2(self):
#         check_list = ['common@example.com', 'commoner@example.com', 'commonest@example.com']
#         result_list = ['hello common', 'hello commoner', 'hello commonest']



