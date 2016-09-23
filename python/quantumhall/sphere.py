import numpy as np
import scipy as sp

# Suggestion for representation of state
(0.145+0.46j, [1,2,3,4])

Q=10

#Enumeration of states simple binary sequence
minState = -1*Q
def Integerize(state):
	return sum(map(lambda orbital: 2**(orbital+minState), state))


def sort(state):
	return np.sort(state)


def valid(state):
	uniqueState = np.unique(state)
	if len(uniqueState) != len(state):
		return False

def same(state1,state2):
	return np.array_equal(state1,state2)


def innerProduct(vec1, vec2):
	if same(vec1[1],vec2[1]):
		return np.conj(vec1[0])*np.conj(vec2[0])
	else:
		return 0

def density1(state):
	def rho(theta, phi):
		orbitallist = map(orbital, state)
		return sum(map(lambda Y: abs(Y(theta,phi))**2, orbitallist))
	return rho

def density2(state):
	statepairs = 
	def rho(theta, phi):
		orbitallist = map(orbital, state)
		return sum(map(lambda Y: abs(Y(theta,phi))**2, orbitallist))
	return rho

import itertools
def kron(l1, l2):
	return itertools.product(l1,l2)

def laughlin3():


def densityMatrix1(state):
	def rho(theta1, phi1, theta2,phi2):
		orbitallist = map(orbital, state)
		return sum(map(lambda Y: Y(theta1,phi1)* np.conj(Y(theta2,phi2)), orbitallist))
	return rho
def orbital(m):
	def u(theta, phi):
		return np.cos(theta/2)* np.exp(0.5j * phi)
	def v(theta, phi):
		return np.sin(theta/2)* np.exp(-0.5j * phi)
	def Y(theta, phi):
		coeff = np.sqrt((2*Q+1)/(4 * np.pi) * sp.special.binom(2*Q, Q-m)) (-1.)**(Q-m)
		return coeff * u(theta phi)**(Q+m) * v(theta,phi)**(Q-m) 
	return Y



