class PayrollSystem:

    def calculate_payroll(self, employees):
        print('Claculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check Amount: {employee.calculate_payroll()}')
            print('')


class SalaryPolicy:

	def __init__(self, weekly_salary):
		self.weekly_salary = weekly_salary

	def calculate_payroll(self):
		return self.weekly_salary


class HourlyPolicy():

    def __init__(self, hours_worked, hourly_rate):
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate


class CommissionPolicy(SalaryPolicy):

    def __init__(self, weekly_salary, commission):
        super().__init__(weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        return super().calculate_payroll() + self.commission
