import unittest
from program.productivity import (
    productivity_system,
    get_role,
    track,
    ManagerRole,
)
from program.employees import _EmployeeDatabase


class TestProductivitySystem(unittest.TestCase):

    hours = 38
    productivity = productivity_system
    employee_database = _EmployeeDatabase()
    employee_list = employee_database.employees()

    def test_get_role(self):
        role = get_role('manager')
        self.assertTrue(isinstance(role, ManagerRole))

    def test_get_role_bad_input(self):
        with self.assertRaises(ValueError):
            get_role('')

    def test_track(self):
        result = []
        result.append(track(self.employee_list, self.hours))
