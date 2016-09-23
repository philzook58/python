
class Operator():
	def __init__(self, func=(lambda state: state)):
		self.func = func 
	def __call__(self, state):
		if type(state) = Operator:
			pass
		else type(state)= State:
			pass
	#def bind(self, monadic):
	#	return Moadic(self.func)
	def __mult__(self, state):
		self.__call__(state)


#Combine this with thunking? For lazy evaulation. Should only evaluate when it knows what to do

#a * a * a = a(a(a()))
