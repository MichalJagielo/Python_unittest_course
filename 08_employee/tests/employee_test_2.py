import unittest
from employee.employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        print('setting up...')
        self.employee = Employee('Jan', 'Nowak', 80000)

    def tearDown(self):
        print('tearing down...')
        del self.employee

    def test_email(self):
        self.assertEqual(self.employee.email, 'jan.nowak@mail.com')

    def test_email_after_change_fname(self):
        self.employee.first_name = 'John'
        self.assertEqual(self.employee.email, 'john.nowak@mail.com')

    def test_email_after_change_lname(self):
        self.employee.last_name = 'Kowalski'
        self.assertEqual(self.employee.email, 'jan.kowalski@mail.com')

    def test_tax(self):
        self.assertEqual(self.employee.tax, 13600)

    def test_salary_after_bonus(self):
        self.employee.apply_bonus()
        self.assertEqual(self.employee.salary, 88000)