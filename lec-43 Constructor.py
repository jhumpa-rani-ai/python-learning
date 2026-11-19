class person:
    name = "harry"
    occ = "developer"

    def info(self):
        print(F"(self.name) is a (self.occ)")

a = person()
a.name = "divya"
a.occ = "HR" 
a.info()       