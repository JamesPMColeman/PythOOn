import unittest
from program import hr


class TestHr(unittest.TestCase):

    def test_Employee(self):
        id = 1
        name = 'Tom Hanks'
        test_employee = hr.Employee(id, name)


        self.assertEqual(test_employee.id, id)
        self.assertEqual(test_employee.name, name)