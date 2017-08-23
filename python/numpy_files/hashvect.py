class HashVect():
	def __init__(self):
		self.v = {}

	def __add__(self,b):
		for k,v in b.v:
			if k in self.v:
				self.v[k] += v
			else:
				self.v[k] = v

	def s_mult(self,a):
		for key,value in self.v:
			self.v[key] = value * a
		# may want to test if map based over self.v.iteritems() is faster?
		#return map( lambda k,v: v*a  , self.v.iteritems())
		# also

	def bind(self, linOp):
		newVect = HashVect()
		for key,value in self.v:
				tempvec = linOP(key)
				tempvec.s_mult(value)
				newVect + tempvec
		return newVect

	def __repr__(self):
		return repr(self.v)






