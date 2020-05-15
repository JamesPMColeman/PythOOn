import hr
import employees
import productivity


manager = employees.Manager(1, 'Michae Scott', 2400)
secretary = employees.Secretary(1, 'Pam Beasly', 1200)
sales_person = employees.SalesPerson(3, 'Andy Bernard', 600, 545)
factory_worker = employees.FactoryWorker(2, 'Roy Anderson', 35, 23.40)
temporary_secretary = employees.TemporarySecretary(5, 'Ryan', 30, 22)

staff = [manager, secretary, sales_person, factory_worker, temporary_secretary]

payroll = hr.PayrollSystem()
payroll.calculate_payroll(staff)

production = productivity.ProductivitySystem()
production.track(staff, 35)
