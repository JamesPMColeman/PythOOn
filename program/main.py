import json
from hr import PayrollSystem
from employees import EmployeeDatabase
from productivity import ProductivitySystem


# productivity_system = ProductivitySystem()
# payroll_system = PayrollSystem()
# employee_database = EmployeeDatabase()
# employees = employee_database.employees()
# productivity_system.track(employees, 40)
# payroll_system.calculate_payroll(employees)

def print_dictionary(employee_as_dict):
	print(json.dumps(employee_as_dict, indent=2))

for employee in EmployeeDatabase().employees():
	print_dictionary(employee.to_dict())