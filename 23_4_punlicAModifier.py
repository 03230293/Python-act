class PAC:
	def _init_(self, x):
		self.v = x  # Public data members
	def displayX(self):
	    print(self.v) #accessible only in class

obj = PAC()
obj.displayX()
