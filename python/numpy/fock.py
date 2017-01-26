from hashvect2 import HashVect
import numpy as np
N = 10
x1 = 1
x2 = 3
state = HashVect()

state[()]=1.
#state[(x1,x2)] = 1.

def adag(x):
	def adagfun(occupation):
		if x in occupation:
			return HashVect({})
		else:
			phase = (-1.) ** len(filter(lambda y: x < y, occupation))
			temp = list(occupation)
			temp.append(x)
			newocc= tuple(sorted(temp))		
			return HashVect({newocc: phase})
	return adagfun

def a(x):
	def afun(occupation):
		if x in occupation:
			phase = (-1.) ** len(filter(lambda y: x < y, occupation))
			newocc = filter(lambda y: y != x, occupation)	
			return HashVect({newocc: phase})	
		else:
			return HashVect({})
	return afun

print state.bind(adag(1)).bind(adag(0))

print adag(1) * (adag(0) * state)


def opPlus(op1, op2):
	def opsum(occupation):
		return op2(occupation).add_in_place(op1(occupation))
	return opsum 

def V(i,j):
	return 1.

def Vop(state):
	return (adag(i) * (adag(j) * (a(j) * (a(i) * state)))).s_mult_in_place(V(i,j))

# may want to use imap? and such?

def dictmap(f, state):
	# f is of form lambda (occ,amp): 
	return HashVect(map(f, state.iteritems()))

def keymap(f, state):
	return dictmap(lambda (occ,val): (f(occ), val), state)

def valmap(f,state):
	return dictmap(lambda (occ,val): (occ, f(val)), state)

def vecsum(states):
	return reduce(lambda a,b: a.sum_in_place(b), states)

def diagonalop(f):
	return lambda state: dictmap(lambda (k,v): (k, v*f(k)), state)



def V2(state):
	def vfun(occ):
		v = sum(map(lambda i:  sum(map(lambda j: 1./(i-j) ,occ[i:])),    occ)) #first sum map is over i second sum map is j>i
		return v

	return diagonalop(vfun)(state)

#single particle hamiltonian
def H1(x):
	t = 0.5
	e = 1.0
	state = HashVect()
	state[x+1] = t
	state[x-1] = t
	state[x] = e
	return state


def matrixElements(A, inList, outList):
	outDict = dict( map( lambda p: p[::-1], enumerate(outList) )) #for fast lookup of index corresponding to key
	# enumerate returns list of tuples (0, key), (1,key2), ...
	H = np.zeros((len(outList),len(inList))
	for i in range(len(inList)):
		state = A(inList[i])
		for k,v in state:
			if k in outDict:
				H[outDict[k],i] = v
	return H

def HFree(occ):
	pass


#thoughts. Apply H to every possible single particle vector. This gives matrxi elements of H
# Heff = H0 - V(1/(H+V)) V expand out V in powers series
# assumes that I can
# V should not be written in terms of adag a unlesss we change how those work. Well.. sacrfice power for speed.
# external sources: J adag
# Write everything in terms of single particle energy basis? So that it is easy to do 1/H
# If single particle is uniform, can use fft
# need to be doing infnite summations. RPA and such. Hubbard Strat to include plasmons?
#

# renormalization approach: Regulate. Keep pertinenet parameters fixed. 
