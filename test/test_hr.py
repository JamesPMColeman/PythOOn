import unittest
from program.hr import (
    payroll_system,
    get_policy,
    calculate_payroll,
    DisabilityPolicy,
)
from program.employees import employee_database


class TestHr(unittest.TestCase):

    employee_db = employee_database
    employee_list = employee_db.employees()
    system = payroll_system

    def test_get_policy(self):
        result = []
        for e in self.employee_list:
            result.append(get_policy(e.identification))
        self.assertIsNotNone(result)

    def test_get_policy_with_bad_input(self):
        with self.assertRaises(ValueError):
            get_policy(0)

    def test_calculate_payroll(self):
        result = calculate_payroll(self.employee_list)
        self.assertIsNone(result)


class TestDisabilityPolicy(unittest.TestCase):

    def test_DisabilityPolicy_without_base_policy(self):
        with self.assertRaises(RuntimeError):
            disability = DisabilityPolicy()
            disability.track_work(40)

    employee_db = employee_database
    employee_list = employee_db.employees()

    sales_employee = employee_list[2]
    disability = DisabilityPolicy()
    sales_employee.apply_payroll_policy(disability)

    def test_track_work(self):
        result = self.disability.track_work(40)
        self.assertIsNone(result)

    def test_calculate_payroll(self):
        result = self.disability.calculate_payroll()
        self.assertEqual(result, 360.0)
        