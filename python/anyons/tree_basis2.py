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


def split(tree, n, a, b): #anyonic Splitting at leaf n into particle a nd b
	
def fuse(tree, n, c): #anyonic fusing of n and n+1 into c. be careful about the end
	pass
def braidover(tree, n): #braid leaf n and n+1, with n going over n+1
	pass
def braidunder(tree, n):# braid leaf n and n+1 with n going under n+1
	pass

