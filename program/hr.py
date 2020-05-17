class PayrollSystem:

    def __init__(self):
        self._employee_policies = {
        1: SalaryPolicy(1000),
        2: SalaryPolicy(950),
        3: CommissionPolicy(600, 100),
        4: HourlyPolicy(40, 22),
        5: HourlyPolicy(35, 16),
    }

    def get_policy(self, employee_id):
        policy = self._employee_policies.get(employee_id)
        if not policy:
            raise ValueError('invalid employee_id')
        return policy

    def calculate_payroll(self, employees):
        print('Claculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check Amount: {employee.calculate_payroll()}')
            if employee.address:
                print('- Sent to')
                print(employee.address)
            print('')


class PayrollPolicy:

    def __init__(self):
        self.hours_worked = 0

    def track_work(self, hours):
        self.hours_worked += hours


class SalaryPolicy(PayrollPolicy):

    def __init__(self, weekly_salary):
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyPolicy(PayrollPolicy):

    def __init__(self, hours_worked, hourly_rate):
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate


class CommissionPolicy(SalaryPolicy):

    def __init__(self, weekly_salary, commission_per_sale):
        super().__init__(weekly_salary)
        self.commission_per_sale = commission_per_sale

    def commission(self):
        sales = self.hours_worked / 5
        return sales * commission_per_sale

    def calculate_payroll(self):
        return super().calculate_payroll() + self.commission
