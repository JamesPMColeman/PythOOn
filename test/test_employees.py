import unittest
from program.employees import Employee, EmployeeDatabase


class TestEmployees(unittest.TestCase):

    employee_database = EmployeeDatabase()
    employee_list = employee_database.employees()
        
    def test_employees(self):
        self.assertTrue(isinstance(self.employee_list[0], Employee))

    def test_calculate_payroll(self):
        result = []
        for e in self.employee_list:
            result.append(e.calculate_payroll())
        self.assertIsNotNone(result)