import unittest
from program import employees


class TestEmployees(unittest.TestCase):

    def test_Employee(self):
        id = 1
        name = 'Tom Hanks'
        test_employee = employees.Employee(id, name)

        self.assertEqual(test_employee.id, id)
        self.assertEqual(test_employee.name, name)

    def test_SalaryEmployee(self):
        id = 2
        name = 'Selma Hyak'
        salary = 1000
        test_employee = employees.SalaryEmployee(id, name, salary)
        result = test_employee.calculate_payroll()

        self.assertEqual(test_employee.id, id)
        self.assertEqual(test_employee.name, name)
        self.assertEqual(test_employee.weekly_salary, salary)
        self.assertEqual(result, salary)

    def test_HourlyEmployee(self):
        id = 3
        name = 'Aurthor C Clark'
        hours = 20
        pay_rate = 25
        test_employee = employees.HourlyEmployee(id, name, hours, pay_rate)
        result = test_employee.calculate_payroll()

        self.assertEqual(test_employee.id, id)
        self.assertEqual(test_employee.name, name)
        self.assertEqual(test_employee.hours_worked, hours)
        self.assertEqual(test_employee.hourly_rate, pay_rate)
        self.assertEqual(result, 500)

    def test_CommissionEmployee(self):
        id = 4
        name = 'Phillip J Fry'
        salary = 500
        commission = 350
        test_employee = employees.CommissionEmployee(id, name, salary, commission)
        result = test_employee.calculate_payroll()

        self.assertEqual(test_employee.id, id)
        self.assertEqual(test_employee.name, name)
        self.assertEqual(test_employee.weekly_salary, salary)
        self.assertEqual(test_employee.commission, commission)
        self.assertEqual(result, 850)