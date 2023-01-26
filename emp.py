class Employee:
    # A data member to count the number of Employees is created
    Empcount = 0
    salaries = []
    
    # A constructor is created to initialize name, family, salary, department
    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.Empcount += 1

#Appending them to a list        
        Employee.salaries.append(self.salary)
    
    # Function to average salary
    def average_salary(self):
        return sum(Employee.salaries) / Employee.Empcount

# Another class Fulltime Employee is created and it inherits the properties of Employee class
class FulltimeEmployee(Employee):
    pass

# Creating the instances of Fulltime Employee class and Employee class 
e1 = Employee("Harry", "StylEs", 8500, "IT")
e2 = FulltimeEmployee("Tom", "Felton", 7860, "CS")
e3 = Employee("revanth","Suryakantam",3450,"HR")

# Calling functions
print(e1.average_salary())
print(e2.average_salary())