import unittest
from program import hr, employees, contacts


class TestHr(unittest.TestCase):

    employee_database = employees._EmployeeDatabase()
    employee_list = employee_database.employees()
    system = hr._PayrollSystem()

    def test_get_policy(self):
        result = []
        for e in self.employee_list:
            result.append(self.system.get_policy(e.id))
        self.assertIsNotNone(result)

    def test_get_policy_with_bad_input(self):
        with self.assertRaises(ValueError):
            self.system.get_policy(0)

    def test_calculate_payroll(self):
        result = self.system.calculate_payroll(self.employee_list)
        self.assertIsNone(result)
        