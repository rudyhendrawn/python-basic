class Employee:
    """Basic procedure of creating a class""" # class docstring
    empCount = 0
    
    def __init__(self, firstname, lastname, salary): # Constructor
        """
            *firstname is first name of the employee
            *lastname is last name of the employee
        """
        self.firstname = firstname 
        self.lastname = lastname
        self.salary = salary
        Employee.empCount += 1
    
    def displayCount(self): # Method 1
        """Display Number of Employees"""
        print('Total Employee %d ' % Employee.empCount)
        
    def displayEmployee(self): # Method 2
        print('Full Name: ', self.firstname, self.lastname, ', Salary: ', self.salary)




   
        






















    
# emp1 = Employee('Zara', 2000)
# emp2 = Employee('Manni', 5000)

# emp1.displayEmployee()
# emp2.displayEmployee()
# print ('Total Employee %d' % Employee.empCount)

# emp3 = EmployeePosition('John', 'Manager', 2000)
# emp3.displayEmployee()
# print ('Total Employee %d' % Employee.empCount)
