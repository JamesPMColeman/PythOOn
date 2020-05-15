class Employee():

    def __init__(self, id, name):
        self.id = id
        self.name = name


class SalaryEmployee(Employee):

    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyEmployee(Employee):

    def __init__(self, id, name, hours_worked, hourly_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate


class CommissionEmployee(SalaryEmployee):

    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        return super().calculate_payroll() + self.commission


class Manager(SalaryEmployee):

    def work(self, hours):
        print(f"Yells at their employees {hours} any time they need a boost")


class Secretary(SalaryEmployee):

    def work(self, hours):
        print(f'Does paper work and greets visiters  {hours} a day')


class SalesPerson(CommissionEmployee):

    def work(self, hours):
        print(f'Spends {hours} hours a day on the phone')


class FactoryWorker(HourlyEmployee):

    def work(self, hours):
        print(f'Prepares products for shipment {hours} a day')


class TemporarySecretary(Secretary, HourlyEmployee):

    def __init__(self, id, name, hours_worked, hourly_rate):
        HourlyEmployee.__init__(self, id, name, hours_worked, hourly_rate)

    def calculate_payroll(self):
        return HourlyEmployee.calculate_payroll(self)