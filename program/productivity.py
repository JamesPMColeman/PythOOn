class _ProductivitySystem:

    def __init__(self):
        self._roles = {
        'manager': ManagerRole,
        'secretary': SecretaryRole,
        'sales': SalesRole,
        'factory': FactoryRole,
    }

    def role(self, role_id):
        role_type = self._roles.get(role_id)
        if not role_type:
            raise ValueError('invalid role_id: ' + role_id)
        return role_type()

    def track(self, employees, hours):
        print('Tracking Employee Productivity')
        print('==============================')
        for employee in employees:
             employee.work(hours)
        print('')


class ManagerRole:

    def work(self, hours):
        """Return a string of the manager's role"""
        return f"Yells at their employees {hours} any time they need a boost"


class SecretaryRole:

    def work(self, hours):
        """Return a string of the secretary's role"""
        return f'Does paper work and greets visiters {hours} a day'


class SalesRole:

    def work(self, hours):
        """Return a string of sales' role"""
        return f'Spends {hours} hours a day on the phone'


class FactoryRole:

    def work(self, hours):
        """Return a string of the factory worker's role"""
        return f'Prepares products for shipment {hours} a day'


productivity_system = _ProductivitySystem()


#Public interface
def get_role(role_id):
    """Return a role based on the employee's id"""
    return productivity_system.role(role_id)


def track(employees, hours):
    """Print out of the employee's tracked work based on input hours"""
    productivity_system.track(employees, hours)
