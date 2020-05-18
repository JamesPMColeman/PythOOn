"""Office control center."""
import json
from hr import calculate_payroll, DisabilityPolicy
from employees import employee_database, Employee
from productivity import track


def print_dictionary(employee_as_dict):
    """Print a dictionary representation of the employee."""
    print(json.dumps(employee_as_dict, indent=2))

employees = employee_database.employees()

sales_employee = employees[2]
disability = DisabilityPolicy()
sales_employee.apply_payroll_policy(disability)

track(employees, 35)
calculate_payroll(employees)

temp_secretary = Employee(5)
print('Temporary Secretary:')
print_dictionary(temp_secretary.to_dict())
