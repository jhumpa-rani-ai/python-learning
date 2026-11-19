class Employee:
    def __init__(self):
        self.__name = "Yashna2"

a = Employee()
# print(a.__name) #cannot be accesed directly
print(a._Employee__name)


# class student:

#     def __init__ (self , age, name):
#         self.age = age       #public varialbe
#         self.name = name        #public varialbe
# obj = student(21,"yashna")    
# print(obj.age)
# print(obj.name)