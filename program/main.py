import hr


salary_employee = hr.SalaryEmployee(1, 'Dan Brigby', 75000)
hourly_employee = hr.HourlyEmployee(2, 'Anna Kramer', 35, 23.40)
commis_employee = hr.CommissionEmployee(3, 'Art Vandaly', 24000, 545)

staff = [salary_employee, hourly_employee, commis_employee]

payroll = hr.PayrollSystem()

payroll.calculate_payroll(staff)
