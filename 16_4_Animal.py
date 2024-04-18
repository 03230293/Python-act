class animal:
    def getAnimal(self):    
        print("Cat and dogs are animals")

class cat (animal):
    def getCat(self):
        print("Cat meows")

class Dog(animal):
    def getDog(self):
        print("Dog barks")

A= animal()
A.getAnimal()
C=cat()
C.getCat()
D=Dog()
D.getDog()