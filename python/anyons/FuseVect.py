import copy


class HashVect(dict):

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

	def s_mult(self,a)
		return HashVect(map(lambda (k,v): (k,v*a)  , self.iteritems()))

	def __rmul__(self, linOp):
		return self.bind(linOp)

	def bind(self, linOp):
		newVect = HashVect()
		for key,value in self.iteritems():
				tempvec = linOp(key)
				tempvec.s_mult_in_place(value)
				newVect.add_in_place(tempvec)
		return newVect

	#Lifts a function on keys to a function on HashVects
	def lift(f):
		newVect = HashVect()
		for key, value in self.iteritems():
				newVect[f(key)] = value
		return newVect


	def unit(self, tree):
		return HashVect({tree: 1.0})

	# A Constructor of the product of Hash
	def fuse(self, ltree, newroot, rtree):
		return HashVect.unit((ltree,newroot,rtree))

'''
	def lbind(self, linOp):
		newVect = HashVect()
		for key,value in self.iteritems():
				ltree = key[0]
				c = key[1]
				rtree = key[2]
				tempvec = linOp(ltree)
				tempvec.s_mult_in_place(value)
				tempvec = tempvec.bind(lambda treea: HashVect.fuse(treea,c,rtree))
				newVect.add_in_place(tempvec)
		return newVect
'''
	def lbind(self, linOp):
		return self.bind(lambda (ltree,c,rtree): linOp(ltree).bind(lambda ltree2: HashVect.fuse(ltree2,c,rtree)))

	def rbind(self, linOp):
		return self.bind(lambda (ltree,c,rtree): linOp(rtree).bind(lambda rtree2: HashVect.fuse(ltree,c,rtree2)))
		
