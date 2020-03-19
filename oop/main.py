from employee import Employee
from employee_position import EmployeePosition

employee_1 = Employee('Peter', 'Parker', 100000)
employee_1.displayCount()
employee_1.displayEmployee()
employee_2 = Employee('Tony', 'Stark', 10000000)
employee_2.displayCount()
employee_2.displayEmployee()

employee_3 = EmployeePosition('Bruce', 'Banner', 'General Manager', 1000000)
employee_3.displayEmployee()