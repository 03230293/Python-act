class Human:
    def setGender(self, g):
        self.gender = g
    def getGender(self):	
        return self.gender

obj1 = Human()
obj1.setGender("Male")
print(obj1.getGender())
obj2 = Human()
obj2.setGender("Female")
print(obj2.getGender())
