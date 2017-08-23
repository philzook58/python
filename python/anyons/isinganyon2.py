#from hashvect2 import HashVect
from FuseVect import HashVect
import numpy as np

psi = 1
I = 0
sigma = 2

exampletree = ((), psi, ((), psi, ()))


def leftFMove(tree):
	tree = list(tree)
	tree = leftCut(tree)

	rootParticle = tree[1]
	
	ltree = tree[0]
	lParticle = ltree[1]

	rtree = tree[2]
	rParticle = rtree[1] #This is the inner particle that will transform
	
	rltree = right[0]
	rlParticle = rltree[1]
	
	rrtree = right[2]
	rrParticle = rrtree[1]

	return ((left,rightroot,rightleft), root , rightright)

	root = tree[1]
	left = tree[0][0][1]
	middle = tree[0][2][1]
	right = tree[2][1]
	inneredge = tree[0][1]



	#organized by root then leaves
	#There are only 4 special cases. Otherwise just fix the inner edge to copmply with
	#fusion rules and returns a 1.

	if root == sigma:
		if lParticle == sigma and middle = sigma and right == sigma:
				tree[0][1] = I
				treeI = tuple(tree)
				tree[0][1] = psi
				treePsi = tuple(tree)
			if inneredge == I:
				return HashVect({treeI: 1/np.sqrt(2), treePsi: 1/np.sqrt(2)})
			if inneredge == psi:
				return HashVect({treeI: 1/np.sqrt(2), treePsi: -11/np.sqrt(2)})
		elif lParticle == psi and middle = sigma and right == psi:
			return HashVect({tuple(tree):-1.0})
		else:
			tree[0][1] = fixFuse(middle, lParticle)
	elif root == psi:
		if lParticle == sigma and middle = psi and right == sigma:
			return HashVect({tuple(tree):-1.0})
		else:
			tree[0][1] = fixFuse(middle, lParticle)
	elif root == I:
		tree[0][1] = fixFuse(middle, lParticle)

		return HashVect({tuple(tree): 1.0})
	tree = tuple(tree)
	return HashVect({tree: 1.0}) 


#suppose v is a hashvect
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




