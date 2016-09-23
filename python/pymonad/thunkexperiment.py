

class Thunk():
	def __init__(self, f=None, args = (), val = None ):
		self.f = f
		self.args = args
		if val:
			self.evaluated = True
		else:
			self.evaluated = False
		self.val = val

	def value(self):
		if not self.evaluated:
			self.val = self.f(*self.args)
			print self.val
		return self.val

	def cobind(self):
		pass

# can either demand eveything takes and returns thunks
# or can demand that function application 


#only ask for .value when you really need it
# like if a or b
# don't evaluated b if if comes back true
import sys


a = Thunk(lambda: 3)
b = Thunk(lambda: 4)
c = Thunk(lambda: 5)

# write functions that only get called when you really really need the value

def plus(x,y):
	if y.f == plus:
		return y.args[1].value() + thunkPlus(x,y.args[0]).value() 

	else:
		return x.value() + y.value()
thunkPlus = lambda x,y: Thunk(plus, args=(x,y))
aplusb = thunkPlus(a,b)

print aplusb
print aplusb.value()

print "a + (b + c)"
thunkPlus(a,thunkPlus(b,c)).value()
print "(a + b) + c"
thunkPlus(thunkPlus(a,b),c).value()


#Infinite List Thunk
def nextOne(val = 0):
	return val, Thunk(nextOne, args=(val+1,))

integers = Thunk(nextOne)


def take(n, mylist):
	returnlist = []
	for i in range(n.value()):
		val, remainder = mylist.value()
		returnlist.append(val)
		mylist = remainder
	return returnlist

firstfive = Thunk(take, args=(c,integers))
print firstfive.value()

#This is laborious and error prone

