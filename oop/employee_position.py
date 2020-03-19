from employee import Employee

class EmployeePosition(Employee):
    def __init__(self, firstname, lastname, position, salary):
        self.position = position
        Employee.__init__(self, firstname, lastname, salary)
        Employee.empCount += 1
        
        if self.position == 'Staf':
            self.salary = salary
        elif self.position == 'Manager':
            self.salary = salary * 2
        elif self.position == 'General Manager':
            self.salary = salary * 3
    
    def displayEmployee(self):
        print('Full Name: ', self.firstname, self.lastname) 
        print('Position: ', self.position)
        print('Salary: ', self.salary)