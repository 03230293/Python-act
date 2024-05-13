#muli-level
class Animal: #BAse
    def speak (self):
        print("Animal Speak")
class dog (Animal): #inheriting the Animal Intermediated clsas
    def bark(self):
        print("Dog Barks")
class labrador (dog): #derived class
    def color (self):
        print ("Labrador is black")
labrador=labrador()
labrador.color()
labrador.bark()
labrador.speak()

#MULTIPLE no intermediated class 
class bird:
    def fly(self):
        print("Bird can fly")
class MAmmal:
    def walk(self):
        print("Mammal can walk")

class Bat(bird, MAmmal):
    def echolocation(self):
        print("Bats uses echolocation")
bat=Bat()
bat.fly()
bat.walk()
bat.echolocation()
