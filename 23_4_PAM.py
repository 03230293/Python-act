class PAM:
	_name = None
	def __init__ (self,name): 
		self.name = name
	def _displayName(self):
		print(self.name)
		 #Derived class        

class PAM_dc(PAM):
	def __init__ (self,name):
		PAM.__init__(self,name)
	def displayD(self):
		self._displayName()
		
Obj = PAM_dc("BIA101") #"BIA101"
Obj.displayD()
