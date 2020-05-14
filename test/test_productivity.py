import unittest
from program import employees, productivity


class TestProductivity(unittest.TestCase):

    salary_employee = employees.Manager(1, 'Michael Scott', 75000)
    hourly_employee = employees.FactoryWorker(2, 'Devon White', 35, 23.40)
    commis_employee = employees.SalesPerson(3, 'Jim Halpert', 24000, 545)
    staff = [salary_employee, hourly_employee, commis_employee]

    def test_ProductivitySystem(self):
        hours_worked = productivity.ProductivitySystem()
        hours_worked.track(self.staff, 35)
