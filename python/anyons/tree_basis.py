import numpy as np

Id = 0
Tau = 1

amp = 1.
vacuumtree =   { leaves : [Id] , stalk: [Id,Id]    } # _|_
# Stalk always has one more element than leaf
examplevector = [( amp , exampletree )]


def N(a,b,c): # number of ways a and b can combine into c. We'll work with ising for now where always 0 or 1
	pass
'''
def split(tree, n, a, b): #anyonic Splitting at leaf n into particle a nd b
	c = tree.leaves[n]
	if N(a,b,c):
		return [(1., {leaves:  }  )]
	else:
		return [(0, {leaves:[], stalk: []} )]
	pass
def fuse(tree, n, c): #anyonic fusing of n and n+1 into c. be careful about the end
	pass
def braidover(tree, n): #braid leaf n and n+1, with n going over n+1
	pass
def braidunder(tree, n):# braid leaf n and n+1 with n going under n+1
	pass
def fmove(subtree): #subtree is a -> b,c, 
'''

def split(tree, n, a, b):
	c = tree.leaves[n]
	if N(a,b,c):
		tree.leaves[n] = a
		tree.leaves.insert(n+1, b)

		F = fmatrix(a,b, tree.stalk[n], tree.stalk[n+1])
		qamp = F[c,:]
		# return qamp list with q taking on the vairous value in tree
		q = Tau
		tree.stalk.insert(n+1, q) # we insert a new stalk edge before the former n+1
		# The actual implementation will be a sum over possible q given by F moves.
		return tree
	else:
		return None

def fuse(tree, n , c):
	stalkparticle = tree.stalk.pop(n+1) #The stalkparticle is changed in the fmove 
	a = tree.leaves.pop(n)
	b = tree.leaves[n]
	tree.leaves[n] = c #This is the opposite f-move reuiqred to split
	return tree

def braidover(tree, n):
	#B - matrix
	pass

def fmatrix(a,b,c,d): #Returns a mtrix in terms of the inner particle. I believe that a is the top man
# and that b c fuse first into e which then fuses with d to make a
# How in the hell can you do this without getting confused?
	tau = 0.618
	rttau = np.sqrt(tau)
	if a == Id and b == Tau and c == Tau and d == Tau:
		return np.array(1)
	elif a == Tau and b == Tau and c == Tau and d == Tau:
		return np.array([[tau,  rttau],
		                 [rttau, -1 * tau]])
	

# good start would be to build up a tree with splits and then join together in reverse order and see if we get 1.


