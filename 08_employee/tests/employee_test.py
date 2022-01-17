import unittest
from employee.employee import Employee


class TestEmployee(unittest.TestCase):

    def test_email(self):
        employee = Employee('Jan', 'Nowak', 80000)
        self.assertEqual(employee.email, 'jan.nowak@mail.com')

    def test_email_after_change_fname(self):
        employee = Employee('Jan', 'Nowak', 80000)
        employee.first_name = 'John'
        self.assertEqual(employee.email, 'john.nowak@mail.com')

    def test_email_after_change_lname(self):
        employee = Employee('Jan', 'Nowak', 80000)
        employee.last_name = 'Kowalski'
        self.assertEqual(employee.email, 'jan.kowalski@mail.com')

    def test_tax(self):
        employee = Employee('Jan', 'Nowak', 80000)
        self.assertEqual(employee.tax, 13600)

    def test_salary_after_bonus(self):
        employee = Employee('Jan', 'Nowak', 80000)
        employee.apply_bonus()
        self.assertEqual(employee.salary, 88000)