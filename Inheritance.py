class Human:
	def getHuman(self):
          print("I am a human")
class Student(Human):
    def getStudent(self):	
        print("I am a student")
h = Human()
h.getHuman()
s = Student()
s.getHuman()
s.getStudent()
