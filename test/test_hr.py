import unittest
from program import hr, employees, contacts


class TestHr(unittest.TestCase):

    id = 42
    name = 'Michael Scott'
    hours = 20
    salary = 1000
    pay_rate = 25
    commission = 350

    def test_PayrollSystem(self):
        manager = employees.Manager(1, 'Michae Scott', 2400)
        secretary = employees.Secretary(1, 'Pam Beasly', 1200)
        sales_person = employees.SalesPerson(3, 'Andy Bernard', 600, 545)
        factory_worker = employees.FactoryWorker(2, 'Roy Anderson', 35, 23.40)
        temporary_secretary = employees.TemporarySecretary(5, 'Ryan', 30, 22)

        manager.address = contacts.Address(
            '5234 Tuneful st.',
            'Scranton',
            'PA',
            '20983'
        )

        staff = [manager, secretary, sales_person, factory_worker, temporary_secretary]

        payroll = hr.PayrollSystem()

        payroll.calculate_payroll(staff)

    def test_ManagerPolicy(self):
        test_employee = employees.Manager(self.id, self.name, self.salary)
        test_employee.work(self.hours)

    def test_SecretaryPolicy(self):
        test_employee = employees.Secretary(self.id, self.name, self.salary)
        test_employee.work(self.hours)

    def test_SalesPolicy(self):
        test_employee = employees.SalesPerson(self.id, self.name, self.salary, self.commission)
        test_employee.work(self.hours)

    def test_FactoryPolicy(self):
        test_employee = employees.FactoryWorker(self.id, self.name, self.hours, self.pay_rate)
        test_employee.work(self.hours)

    def test_TemporarySecretary(self):
        test_employee = employees.TemporarySecretary(self.id, self.name, self.hours, self.pay_rate)
        test_employee.calculate_payroll()

    def test_get_policy(self):
        system = hr.PayrollSystem()
        policy_object = system.get_policy(1)
        