"""Employee module handles the representation and implemntation of employees"""
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

    def employees(self):
        """Access employees by identification and return them in a list."""
        return [Employee(identify_) for identify_ in sorted(self._employees)]

    def get_employee_info(self, employee_id):
        """Enter employee id and return information about the employee."""
        info = self._employees.get(employee_id)
        if not info:
            raise ValueError('invalid employee id')
        return info


class Employee(DictionaryMixin):
    """
    A class that represents an employee

    Attributes
    ----------
    identification : int
        ID associated with employee and location with in dictionaries
    name : string
        Employee's full name
    address : Address object
        Object representing the Employee's address

    Methods
    -------
    work(hours)
        Prints employee information and tracks work by hours
    calculate_payroll()
        Return info on employee's payroll
    apply_payroll_policy(new_policy)
        Change an employee's payroll policy
    """

    def __init__(self, identification):
        self.identification = identification
        employee_info = employee_database.get_employee_info(identification)
        self.name = employee_info.get('name')
        self.address = get_address(self.identification)
        self._payroll = get_policy(self.identification)
        self._employee_role = get_role(employee_info.get('role'))

    def work(self, hours):
        """Prints employee information and tracks work by hours."""
        tasks = self._employee_role.work(hours)
        print(f'Employee {self.identification} - {self.name}:')
        print(f'- {tasks}')
        print('')
        self._payroll.track_work(hours)

    def calculate_payroll(self):
        """Return info on employee's payroll."""
        return self._payroll.calculate_payroll()

    def apply_payroll_policy(self, new_policy):
        """Change an employee's payroll policy."""
        new_policy.apply_to_policy(self._payroll)
        self._payroll = new_policy


employee_database = _EmployeeDatabase()
