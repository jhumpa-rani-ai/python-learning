
class person:
    name = "Harry"
    network = 10
    def info(self):
        print(f"{self.name} is  a {self.occupation}")

a = person()
b = person()

a.name = "Shubham"
a.occupation = "Accountant"

b.name = "Yashna"
b.occupation = "Software Engineer"
# print(a.name,a.occupation)
a.info()
b.info()
