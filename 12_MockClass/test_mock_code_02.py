import random
import unittest
from unittest.mock import patch
from mock_code_02 import get_nums, get_day_name, get_nums_day_name
from datetime import date


class TestGetNums(unittest.TestCase):

    @patch('random.randint')
    def test_get_nums(self, mock_random):
        mock_random.return_value = 4
        result = get_nums()
        expected = 'XXX-4'
        self.assertEqual(result, expected)


class TestGetDayName(unittest.TestCase):

    def test_get_day_name(self):
        result = get_day_name()
        expected = 'Fri'
        self.assertEqual(result, expected)


class TestGetNumsDayName(unittest.TestCase):

    @patch('random.randint')
    def test_get_nums_day_name_today(self, mock_num):
        mock_num.return_value = 3
        result = get_nums_day_name()
        expected = 'XXX-3-FRI'
        self.assertEqual(result, expected)

    @patch('mock_code_02.get_day_name')
    @patch('random.randint')
    def test_get_nums_mocked_day_name_today(self, mock_num, mock_day):
        mock_num.return_value = 5
        mock_day.return_value = 'TUE'
        result = get_nums_day_name()
        expected = 'XXX-5-TUE'
        self.assertEqual(result, expected)

    @patch('mock_code_02.get_day_name')
    @patch('random.randint')
    def test_get_nums_mocked_day_name_sunday(self, mock_num, mock_day):
        mock_num.return_value = 7
        mock_day.return_value = 'SUN'
        result = get_nums_day_name()
        expected = 'XXX-7-SUN'
        self.assertEqual(result, expected)

