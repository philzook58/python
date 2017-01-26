Nil = 0 #maybe no nil
Id = 1
Tau = 2

# this is not right. we need more labels.
exampletree = (Id, (Tau,  Tau)) # _|_ 

exampletree2 = (  (Id,(Id, (Id,Nil))) ,  (Id, Nil)  ) # root tuple is leaves and stalk ()




def leaves(tree):
	return tree[0]
def stalk(tree):
	return tree[1]

# use consing style



state = {}
state[exampletree] = 1.
# hash is nice since it is a fast way of performing "vector reduction", combining vectors that have same diagram
# in order to use hash must use tuples or other immutable object.
# wrap inside class that checks if key in. If so just add ampltidues

# the porblem with full tree hash storage is that the power of kronecker product reps is the factorizability.
# we need stratification
# so the hash could hold subtrees?
'''
class VectHash():
	def __init__(self, vac):
		self.dict = {vac: 1.}

	def __add__(self, b):
		if len(self) < len(b):
			a = b
			b = self
		else:
			a = self
			b = b

		for key,value in b:
			if key in a:
				a[key] = a[key] + b
	def __getitem__(self, key):
		return self.dict[key]
	def __setitem__(self, key, value):
		self.dict[key] = value
	def __mult__(self, b):
		# if b = anpother VectHash, then take kronecker product. Disjoint graphs? or take identity root and join to their identity root

		pass
'''
class VectHash(dict):
	#add mutates original
	def __add__(self, b):
		if len(self) < len(b):
			a = b
			b = self
		else:
			a = self
			b = b
		# would be nice to do in a map?
		for key,value in b:
			if key in a:
				a[key] = a[key] + value
		return a
	# could store trees with indices which then refer to object list. Object list could hold lower vectHashes 


def cons(a, tree):
	return (a, tree)

def car(tree):
	return tree[0]

def cdr(tree):
	return tree[1]

def indexat(mylist,n):
	if n == 0:
		car(mylist)
	else:
		indexat(cdr(mylist), n-1)


#could use zipper structure. Was kind of nice

#vacuum = cons(Id, Nil)

def fmoveL(subtree): # hand it tree with root at root of fmove
	pass
def fmoveR(subtree):
	pass

def split(tree, n, a, b): #anyonic Splitting at leaf n into particle a nd b
	
def fuse(tree, n, c): #anyonic fusing of n and n+1 into c. be careful about the end
	pass
def braidover(tree, n): #braid leaf n and n+1, with n going over n+1
	pass
def braidunder(tree, n):# braid leaf n and n+1 with n going under n+1
	pass

