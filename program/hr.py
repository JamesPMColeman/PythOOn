class PayrollSystem:

    def calculate_payroll(self, employees):
        print('Claculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check Amount: {employee.calculate_payroll()}')
            print('')
