class RAallowances:
    def setRAallowances(self, RAallowances):
        self.RAallowances=RAallowances /100
    def getRAallowances(self):
        return self.RAallowances 
    
obj1 = RAallowances()
# obj1.setModules("Maths")
# print(obj1.getModules())

obj1.setRAallowances(int(input("Enter RA aloowances your recievd")))
print(obj1.getRAallowances())


# obj2 = student()
# obj2.setModules("English")
# print(obj2.getModules())
    
class houserentallowances:
    def setHAallowances(self, HAallowances):
        self.HAallowances=HAallowances/100
    def getHAallowances(self):
        return self.HAallowances
obj2=houserentallowances()
obj2.setHAallowances(int(input("Enter H a aloowances your recievd")))
print(obj2.getHAallowances())

class total_a:
    def settotal_a(self, HAallowances, RAallowances):
        self.total_a= HAallowances + RAallowances
    def gettotal_a(self):
        return self.total_a
total=total_a()
total.settotal_a(obj1.RAallowances, obj2.HAallowances)
print(total.gettotal_a())