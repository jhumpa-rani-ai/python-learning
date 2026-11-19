class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def showdetails(self):
        print(f'The name of employee:{self.id} id {self.name}')

class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")
              

e1=Employee("Rohan Das",400)
e1.showdetails() 
e2=Employee("Sameer kr",500)
e2.showdetails()
e2.showLanguage()           