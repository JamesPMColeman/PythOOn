import unittest
from program.employees import Employee, employee_database


class TestEmployees(unittest.TestCase):

    employee_db = employee_database
    employee_list = employee_db.employees()
        
    def test_employees(self):
        self.assertTrue(isinstance(self.employee_list[0], Employee))

    def test_calculate_payroll(self):
        result = []
        for e in self.employee_list:
            result.append(e.calculate_payroll())
        self.assertIsNotNone(result)

    def test_get_employee_info_with_bad_input(self):
    	with self.assertRaises(ValueError):
    		self.employee_db.get_employee_info(0)