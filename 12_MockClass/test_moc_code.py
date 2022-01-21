import unittest
from unittest.mock import patch
from mock_code import get_nums


class TestGetNums(unittest.TestCase):

    @patch('random.randint')
    def test_get_nums_mock_should_return_3(self, mock_random):
        mock_random.return_value = 3
        function = get_nums()
        expected = 'num-3'
        self.assertEqual(function, expected)

    @patch('random.randint')
    def test_get_nums_mock_should_return_5(self, mock_random):
        mock_random.return_value = 5
        function = get_nums()
        expected = 'num-5'
        self.assertEqual(function, expected)

    @patch('random.randint')
    def test_get_nums_mock_should_return_9(self, mock_random):
        mock_random.return_value = 9
        function = get_nums()
        expected = 'num-9'
        self.assertEqual(function, expected)


