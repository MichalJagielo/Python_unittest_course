import unittest
from unittest.mock import patch
from mock_method_03 import TechStack


class TestTechStack(unittest.TestCase):

    def setUp(self):
        print('setting test')
        self.stock = TechStack()
        self.stock.add_tech('phone') \
            .add_tech('tv') \
            .add_tech('database') \
            .add_tech('testing') \
            .add_tech('google_cloud') \
            .add_tech('aws')

    def tearDown(self):
        print('tearing down test')


    @patch.object(TechStack, 'get_tech')
    def test_get_tech_01(self, mock_method):
        mock_method.return_value = 'testing'
        result = 'testing'
        expected = self.stock.get_tech()
        self.assertEqual(result, expected)

    @patch.object(TechStack, 'get_tech')
    def test_get_tech_02(self, mock_method):
        mock_method.return_value = 'aws'
        result = 'aws'
        expected = self.stock.get_tech()
        self.assertEqual(result, expected)
