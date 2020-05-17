from hr import PayrollSystem
from contacts import AddressBook
from productivity import ProductivitySystem

class EmployeeDatabase:

    def __init__(self):
        self._employees = [
            {
                'id': 1,
                'name': 'Michae Scott',
                'role': 'manager',
            },
            {
                'id': 2,
                'name': 'Pam Beasly',
                'role': 'secretary',
            },
            {
                'id': 3,
                'name': 'Andy Bernard',
                'role': 'sales',
            },
            {
                'id': 4,
                'name': 'Roy Anderson',
                'role': 'factory',
            },
            {
                'id': 5,
                'name': 'Ryan',
                'role': 'secretary',
            },
        ]
        self.productivity = ProductivitySystem()
        self.employee_address = AddressBook()
        self.payroll = PayrollSystem()

    def employees(self):
        return [self._create_employee(**data) for data in self._employees]
     
    def _create_employee(self, id, name, role):
        address = self.employee_address.get_address(id)
        employee_roll = self.productivity.get_role(role)
        payroll_policy = self.payroll.get_policy(id)
        return Employee(id, name, address, employee_roll, payroll_policy)


class Employee():

    def __init__(self, id, name, address, role, payroll):
        self.id = id
        self.name = name
        self.address = address
        self.payroll = payroll
        self.employee_role = role

    def work(self, hours):
        tasks = self.employee_role.work(hours)
        print(f'Employee {self.id} - {self.name}:')
        print(f'- {tasks}')
        print('')
        self.payroll.track_work(hours)

    def calculate_payroll(self):
        return self.payroll.calculate_payroll() 

