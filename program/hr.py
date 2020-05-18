class _PayrollSystem:

    def __init__(self):
        self._employee_policies = {
        1: SalaryPolicy(1000),
        2: SalaryPolicy(950),
        3: CommissionPolicy(600, 100),
        4: HourlyPolicy(22),
        5: HourlyPolicy(16),
    }

    def _get_policy(self, employee_id):
        policy = self._employee_policies.get(employee_id)
        if not policy:
            raise ValueError('invalid employee_id')
        return policy

    def _calculate_payroll(self, employees):
        print('Calaculating Payroll')
        print('====================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check Amount: {employee.calculate_payroll()}')
            if employee.address:
                print('- Sent to')
                print(employee.address)
            print('')


class DisabilityPolicy:

    def __init__(self):
        self._base_policy = None

    def track_work(self, hours):
        self._check_base_policy()
        return self._base_policy.track_work(hours)

    def calculate_payroll(self):
        self._check_base_policy()
        base_salary = self._base_policy.calculate_payroll()
        return base_salary * 0.6

    def apply_to_policy(self, base_policy):
        self._base_policy = base_policy

    def _check_base_policy(self):
        if not self._base_policy:
            raise RuntimeError('Base policy missing')


class PayrollPolicy:

    def __init__(self):
        self.hours_worked = 0

    def track_work(self, hours):
        self.hours_worked += hours


class SalaryPolicy(PayrollPolicy):

    def __init__(self, weekly_salary):
        super().__init__()
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyPolicy(PayrollPolicy):

    def __init__(self, hourly_rate):
        super().__init__()
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate


class CommissionPolicy(SalaryPolicy):

    def __init__(self, weekly_salary, commission_per_sale):
        super().__init__(weekly_salary)
        self.commission_per_sale = commission_per_sale

    def commission(self):
        sales = self.hours_worked / 5
        return sales * self.commission_per_sale

    def calculate_payroll(self):
        return super().calculate_payroll() + self.commission()


payroll_system = _PayrollSystem()

# Public interface
def get_policy(employee_id):
    return payroll_system._get_policy(employee_id)


def calculate_payroll(employees):
    return payroll_system._calculate_payroll(employees)
