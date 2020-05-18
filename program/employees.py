from program.hr import get_policy
from program.contacts import get_address
from program.productivity import get_role
from program.representations import DictionaryMixin

class _EmployeeDatabase:

    def __init__(self):
        self._employees = {
            1: {
                'name': 'Michae Scott',
                'role': 'manager',
            },
            2: {
                'name': 'Pam Beasly',
                'role': 'secretary',
            },
            3: {
                'name': 'Andy Bernard',
                'role': 'sales',
            },
            4: {
                'name': 'Roy Anderson',
                'role': 'factory',
            },
            5: {
                'name': 'Ryan',
                'role': 'secretary',
            },
        }
        self.productivity = ProductivitySystem()
        self.employee_address = AddressBook()
        self.payroll = PayrollSystem()

    def employees(self):
        return [Employee(id_) for id_ in sorted(self._employees)]
     
    def _create_employee(self, id, name, role):
        address = self.employee_address.get_address(id)
        employee_roll = self.productivity.get_role(role)
        payroll_policy = self.payroll.get_policy(id)
        return Employee(id, name, address, employee_roll, payroll_policy)


class Employee(DictionaryMixin):

    def __init__(self, id, name, address, role, payroll):
        self.id = id
        self.name = name
        self.address = address
        self._payroll = payroll
        self._employee_role = role

    def work(self, hours):
        tasks = self._employee_role.work(hours)
        print(f'Employee {self.id} - {self.name}:')
        print(f'- {tasks}')
        print('')
        self._payroll.track_work(hours)

    def calculate_payroll(self):
        return self._payroll.calculate_payroll() 

