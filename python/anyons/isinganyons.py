from hashvect2 import HashVect
import numpy as np

psi = 1
I = 0
sigma = 2

exampletree = ((), psi, ((), psi, ()))


# These are actually not the operators wanted for anyons
def leftrotate(tree):
	root = tree[1]
	left = tree[0]
	right = tree[2]
	rightroot = right[1]
	rightleft = right[0]
	rightright = right[2]

	return ((left,root,rightleft), rightroot , rightright)

def rightrotate(tree):
	root = tree[1]
	left = tree[0]
	right = tree[2]
	leftroot = left[1]
	leftleft = left[0]
	leftright = left[2]

	return (leftleft, leftroot, (leftright,root,right))

assert leftrotate((0,1,(2,3,4)))  == ((0,1,2),3,4)
assert (0,1,(2,3,4))  == rightrotate(((0,1,2),3,4))

#rotations are inverse operations
assert leftrotate(rightrotate(((0,1,2),3,4))) == ((0,1,2),3,4) 


def leftCut(tree):
	root = tree[1]
	left = tree[0]
	right = tree[2]
	rightroot = right[1]
	rightleft = right[0]
	rightright = right[2]

	return ((left,rightroot,rightleft), root , rightright)


def fixFuse(a, b):
	if a == psi and b == psi:
		return I
	elif a = psi and b = sigma:
		return sigma
	elif a = sigma and b = psi:
		return sigma


#every node is associated with edge leading to it.
#leftrotate is conversion from left side of equation in Kitaev
def leftF(tree):
	tree = list(tree)
	tree = leftCut(tree)
	root = tree[1]
	left = tree[0][0][1]
	middle = tree[0][2][1]
	right = tree[2][1]
	inneredge = tree[0][1]
	#organized by root then leaves
	#There are only 4 special cases. Otherwise just fix the inner edge to copmply with
	#fusion rules and returns a 1.

	if root == sigma:
		if left == sigma and middle = sigma and right == sigma:
				tree[0][1] = I
				treeI = tuple(tree)
				tree[0][1] = psi
				treePsi = tuple(tree)
			if inneredge == I:
				return HashVect({treeI: 1/np.sqrt(2), treePsi: 1/np.sqrt(2)})
			if inneredge == psi:
				return HashVect({treeI: 1/np.sqrt(2), treePsi: -11/np.sqrt(2)})
		elif left == psi and middle = sigma and right == psi:
			return HashVect({tuple(tree):-1.0})
		else:
			tree[0][1] = fixFuse(middle, left)
	elif root == psi:
		if left == sigma and middle = psi and right == sigma:
			return HashVect({tuple(tree):-1.0})
		else:
			tree[0][1] = fixFuse(middle, left)
	elif root == I:
		tree[0][1] = fixFuse(middle, left)

		return HashVect({tuple(tree): 1.0})
	tree = tuple(tree)
	return HashVect({tree: 1.0}) 


assert leftF

def rightF(tree):

#this is expensive. There are a lot of ways to make more efficient
def pathToNLeaf(tree, N):
	if N = 1:
		if tree == ():
			return []
		else:
			return ['L'] + pathtoNLeaf(tree[0], 1)

	leftCount = leafCount(tree[0])
	if leftCount <= N:
		return ['L'] + pathtoNLeaf(tree[0], N)
	else:
		return ['R'] + pathtoNLeaf(tree[2],N - leftCount)


def leafCount(tree):
	if tree == ():
		return 1
	else:
		return leafCount(tree[0]) + leafCount(tree[2])  


def split(leftv, particle, rightv):
	newVect = HashVect()
	for (left, leftval) in leftv.iteritems():
		for (right, rightval) in rightv.iteritems():
			newVect[(left,particle, right)] = leftval * rightval
	return newVect

def rightbind(v, LinOp):
	if tree[2] == ():
		return v
	lefttree = HashVect({tree[0]:1.0})
	righttree = HashVect({tree[2]:1.0})
	return split(lefttree, tree[1],  righttree.bind(LinOp))

def recurseLeftF(tree):
	v = HashVect({tree}: 1.0)
	return rightbind(v, recurseLeftF)

def recurseLeftF(tree):
	v = HashVect({tree}: 1.0)
	return leftbind(v, recurseRightF)


def makesiblings2(tree,a,b):
	if a[path[0]] == b[path[0]]:
		if a[path[0]] == 'L':
			v = traversepath(tree[0])
			return v.keymap(lambda k: (k, tree[1], tree[2]))
		else:
			v = traversepath(tree[2])
			return v.keymap(lambda k: (tree[0], tree[1], k))
	v = HashVect({tree:1.0})
	v = v.bind(recurseLeftF)
	v = v.bind(recurseRightF)
	return v




def makeleavesiblings(tree, n):
	a = pathtoNLeaf(n)
	b = pathtoNLeaf(n+1)
	return makesiblings2(tree,a,b)


#traverse down tree to first divergence of position
'''
	i = 0
	while a[i]==b[i]:
		if a[i] == 'L':
			tree = tree[0]
		else:
			tree = tree[2]
		i += 1

	# now a[i]='L' and b[i]='R'
	assert a[i] == 'L'
	assert b[i] == 'R'
	for move in a[i:]:
		assert move == 'R'
	for move in b[i:]:
		assert move == 'L'
	# and all the rest of a after are 'R'
	# and all the rest after b are 'L'
	i += 1
	v = HashVect({tree:1.0})
	v = v.bind(recurseLeftF)
	v = v.bind(recurseRightF)
	#v.fmap()
	return v
'''
	'''
	for move in a[i:]:
		assert move == 'R'
		v = rightbind(v ,leftF)
		v = v.bind(leftF)
	'''
	# similar for other side

def swapsiblings(tree, path):
	assert len(path) > 0

	if len(path) == 1:
		return (tree[2], tree[1], tree[1])
	else:
		if path[0] == 'L':
			return (swapsiblings(tree[0], path[1:]), tree[1], tree[2])
		else:
			return (tree[0] ,tree[1], swapsiblings(tree[2], path[1:]))





def siblingbraid(tree,N):
	path = pathtoNLeaf(n)
	swappedtree = swapsiblings(tree, path)
	for move in path[0:-1]:
		if move == 'L':
			tree = tree[0]
		else:
			tree = tree[2]
	parent


	

def fuse(tree, N, c):
	v = makeleavesiblings(tree,N)
	v.bind()




def braidleftoverright(tree, N):
	v = makeleavesiblings(tree, N)
	return v.bind(siblingbraid)
	pass
def braidrightoverleft(tree, N):
	#v = braidleftoverright(tree,N)
	#Can I just conjugate something?
	pass

