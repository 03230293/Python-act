class student:
    def setModules(self, m):
        self.Module=m
    def getModules(self):
        return self.Module
    
obj1 = student()
obj1.setModules("Maths")
print(obj1.getModules())
obj2 = student()
obj2.setModules("English")
print(obj2.getModules())

