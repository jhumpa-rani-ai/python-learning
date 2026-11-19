class Employee:
    companyName = "Apple"
    no0fEmployee = 0

    def __init__(self,name):
        self.name = name
        self.raise_amount  =0.02
        Employee.no0fEmployee +=1
    def showDetails(self):
        print(f"The name of the Employee is {self.name and the 
raise amount in {self.no0fEmployee} sized
{self.companyName} is {self.raise_amount}")

emp1 = Employee("Harry")
emp1.raise_amount = 0.3
emp1.comapnyName = "Apple India"
emp1.showDetails()