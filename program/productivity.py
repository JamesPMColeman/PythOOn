class ProductivitySystem:

    def __init__(self):
        self._roles = {
        'manager': ManagerRole,
        'secretary': SecretaryRole,
        'sales': SalesRole,
        'factory': FactoryRole,
    }

    def get_role(self, role_id):
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
        return f"Yells at their employees {hours} any time they need a boost"


class SecretaryRole:

    def work(self, hours):
        return f'Does paper work and greets visiters {hours} a day'


class SalesRole:

    def work(self, hours):
        return f'Spends {hours} hours a day on the phone'


class FactoryRole:

    def work(self, hours):
        return f'Prepares products for shipment {hours} a day'
