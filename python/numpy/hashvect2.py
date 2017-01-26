import copy

#other ideas:

# try using the listvect. Might be more flexible
# store precomposition functions  for hash. Kind of a lazy thing
# could have a function call that just totally evaluates the whole thing
# matrix ops kind of suck.

class HashVect(dict):
#	def __init__(self):
#		self.v = {}

	def __add__(self,b):
		c = copy.copy(self)
		return c.add_in_place(b)

	def add_in_place(self,b):
		for key, value in b.iteritems():
			if key in self:
				self[key] += value
			else:
				self[key] = value
		return self

	def s_mult_in_place(self,a):
		for key,value in self.iteritems():
			self[key] = value * a
		# may want to test if map based over self.v.iteritems() is faster?
	def s_mult(self,a)
		return HashVect(map(lambda (k,v): (k,v*a)  , self.iteritems()))
		# also
	def __rmul__(self, linOp):
		return self.bind(linOp)

	def bind(self, linOp):
		newVect = HashVect()
		for key,value in self.iteritems():
				tempvec = linOp(key)
				tempvec.s_mult_in_place(value)
				newVect.add_in_place(tempvec)
		return newVect

	def kron(self,b):
		newVect = HashVect()
		for key,value in self.iteritems():
				for key2, value2 in b.iteritems():
					newVect[(key,key2)] = value * value2	
		return newVect

	def dekron(self):
		# perform SVD
		# return HashVect indexed by  Kron objects with SVD value as val.
		pass

#	def __repr__(self):
#		return repr(self.v)

class Kron():
	# inspired by monoidal category
	def __init__(self, a,b):
		assert(type(a) is HashVect and type(b) is HashVect)
		self.a = a
		self.b = b

	def expand(self,a,b):
		return a.kron(b)

	def flip(self):
		c = self.a
		self.a = self.b
		self.b = c

	def loseleft(self):
		assert(len(a)==1):
		return self.b


def unit(tree):
	return HashVect({tree:1.0})




