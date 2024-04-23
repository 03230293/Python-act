# Parameterized Constructor
class Employee:
   def __init__(self, name, age): #name and age- parameter of employee
      self.name = name
      self.age = age
e1 = Employee("Thinley", 20)
print (f"Name: {e1.name}")
print (f"age:{e1.age}")