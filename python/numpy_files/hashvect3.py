#Better yet, use a layer of misdirection ad use numpy array on backend
import numpy as np
import copy

#switch out fixed numpy array for sparse
# or use python array. which can be appended
# and easily converted to np.array
class HashVect():
	def __init__(self, size=100):
		self.key2index = {}
		self.index2key = []
		self.data = np.zeros(size)
		self.maxindex = 0

	def __add__(self,b):
		assert(type(b) is HashVect)

		c = HashVect(size=len(self)+len(b))
		#x = max(self,b)
		#y = min(self,b)
		c.data[:len(self)] = self.data
		c.key2index = copy.copy(self.key2index)
		c.index2key = copy.copy(self.index2key)
		c.maxindex = self.maxindex

		for key, value in b.key2index.iteritems():
			if key in self.key2index:
				c.data[c.key2index[key]] += value
			else:
				c[key] = value

	def __getitem__(self, item):
		return self.data[self.key2index[item]]

	def __setitem__(self, item, val):
		if item in self.key2index:
			self.data[self.key2index[item]] = val
		else:
			self.key2index[item] = self.maxindex
			self.index2key.append(item)
			self.data[self.maxindex] = val
			self.maxindex += 1


	def s_mult(self,a):
		self.data = self.data * a 
		return self
		# may want to test if map based over self.v.iteritems() is faster?
		#return map( lambda k,v: v*a  , self.v.iteritems())
		# also
	def __len__(self):
		return len(self.key2index)
	def bind(self, linOp):
		newVect = HashVect()
		for key,value in self.iteritems():
				tempvec = linOP(key)
				tempvec.s_mult(value)
				newVect + tempvec
		return newVect

#	def __repr__(self):
#		return repr(self.v)