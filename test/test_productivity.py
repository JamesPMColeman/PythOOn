import unittest
from program import employees, productivity


class TestProductivitySystem(unittest.TestCase):

    hours = 38
    productivity_system = productivity._ProductivitySystem()
    employee_database = employees._EmployeeDatabase()
    employee_list = employee_database.employees()

    def test_get_role(self):
        role = self.productivity_system.get_role('manager')
        self.assertTrue(isinstance(role, productivity.ManagerRole))

    def test_get_role_bad_input(self):
        with self.assertRaises(ValueError):
            self.productivity_system.get_role('')

    def test_track(self):
        result = []
        result.append(self.productivity_system.track(self.employee_list, self.hours))