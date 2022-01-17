
import unittest


def setUpModule():          # konwencja nazw setUpModule z java
    print('setting up module....')


def tearDownModule():       # konwencja nazw tearDownModule z java
    print('tearing down module...')


class TestClass1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(f'setting up class-{cls.__name__}')

    @classmethod
    def tearDownClass(cls):
        print(f'tearing down class-{cls.__name__}')

    def test_case_1(self):
        self.assertEqual('Ala ma kota'.split(), ['Ala', 'ma', 'kota'])

    def test_case_2(self):
        self.assertEqual('Ala ma kota'.split(), ['Ala', 'ma', 'kota'])

    def setUp(self):
        print('setting up---')

    def tearDown(self):
        print('tearing down---')


class TestClass2(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual('#'.join(['Ala', 'ma', 'kota']), 'Ala#ma#kota')


class TestClass3(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual('444.555'.split('.'), ['444', '555'])


# if __name__ == '__main__':
#     unittest.main(verbosity=2)