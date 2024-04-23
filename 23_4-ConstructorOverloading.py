class ConstructorOverloading:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Create objects with different sets of parameters
obj1 = ConstructorOverloading()
obj2 = ConstructorOverloading("Sonam")
obj3 = ConstructorOverloading("Peydon", 19)
# Display information for each object
obj1.display()  
obj2.display()  
obj3.display()  

#pass input