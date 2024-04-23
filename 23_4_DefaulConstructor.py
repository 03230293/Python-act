# Default Constructor - can"t passvalue to tghe class
class Employee:
   def __init__(self):
      self.name = "Thinley"
      self.age = 20
   def displayEmployee(self):
       x= "Hello" #Variable accessible only inside functions _Function specific the function
       print(x)
       print(f'Name:{self.name} Age:{self.age}')
e1 = Employee()
e1.displayEmployee()



 #sef. - will accessble in outside the method
