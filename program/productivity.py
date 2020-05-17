class ProductivitySystem:

    def track(self, employees, hours):
        print('Tracking Employee Productivity')
        print('==============================')
        for employee in employees:
            result = employee.work(hours)
            print(f'{employee.name}: {result}')
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
