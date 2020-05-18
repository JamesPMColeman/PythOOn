from program.hr import get_policy, payroll_system
from program.contacts import get_address, address_book
from program.productivity import get_role, productivity_system
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

    def employees(self):
        return [Employee(id_) for id_ in sorted(self._employees)]
     
    def get_employee_info(self, employee_id):
        info = self._employees.get(employee_id)
        if not info:
            raise ValueError('invalid employee id')
        return info


class Employee(DictionaryMixin):

    def __init__(self, id):
        self.id = id
        employee_info = employee_database.get_employee_info(id)
        self.name = employee_info.get('name')
        self.address = get_address(self.id)
        self._payroll = get_policy(self.id)
        self._employee_role = get_role(employee_info.get('role'))

    def work(self, hours):
        tasks = self._employee_role.work(hours)
        print(f'Employee {self.id} - {self.name}:')
        print(f'- {tasks}')
        print('')
        self._payroll.track_work(hours)

    def calculate_payroll(self):
        return self._payroll.calculate_payroll() 


employee_database = _EmployeeDatabase()

