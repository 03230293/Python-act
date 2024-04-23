class PrivateAM:
  	# private members
     __name = None
     def __init__(self, name): 
          self.__name = name
# private member function 
     def __displayDetails(self):
           print("Name: ", self.__name)# Private Access Modifier
#Not accessible outside the class
           
# Private Access Modifier
# public member function double _ 
     def accessPrivateFunction(self):
          # accessing private member function
           self.__displayDetails() 
 
#  creating object	
obj = PrivateAM("Hello")
 
# calling public member function of the class
obj.accessPrivateFunction()

