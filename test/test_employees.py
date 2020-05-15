import io
import sys
import unittest
from program import employees


class TestEmployees(unittest.TestCase):

    id = 42
    name = 'Michael Scott'
    hours = 20
    salary = 1000
    pay_rate = 25
    commission = 350

    def test_Employee(self):
        test_employee = employees.Employee(self.id, self.name)

        self.assertEqual(test_employee.id, self.id)
        self.assertEqual(test_employee.name, self.name)

    def test_Manager(self):
        test_employee = employees.Manager(self.id, self.name, self.salary)
        test_employee.work(self.hours)

    def test_Secretary(self):
        test_employee = employees.Secretary(self.id, self.name, self.salary)
        test_employee.work(self.hours)

    def test_SalesPerson(self):
        test_employee = employees.SalesPerson(self.id, self.name, self.salary, self.commission)
        test_employee.work(self.hours)

    def test_FactoryWorker(self):
        test_employee = employees.FactoryWorker(self.id, self.name, self.hours, self.pay_rate)
        test_employee.work(self.hours)

    def test_TemporarySecretary(self):
        test_employee = employees.TemporarySecretary(self.id, self.name, self.hours, self.pay_rate)
        result = test_employee.calculate_payroll()
        