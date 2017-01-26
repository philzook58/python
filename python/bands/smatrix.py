import numpy as np

import scipy as sp
from scipy import linalg as spLA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from numpy import linalg as LA
from matplotlib.ticker import LinearLocator, FormatStrFormatter



# s matrix formulation
delta = 0.1


def GRet(E):
	return LA.inverse(H - np.eye(H)*E + 1.j * delta)

def GAdv(E):
	return np.conjugate(GRet(E))

def DensityofStates(E):
	G = GRet(E)
	return np.trace(G-np.conjugate(G))

N = 100

t1 = 1.5
t2 = -0.5

bands = 2

C =np.roll(np.eye(N),1,axis=0) # circulant off diagonal matrices
CT = np.transpose(C) 

temp = np.zeros(N)
temp[1] = 1.0
T = spLA.toeplitz(temp, np.zeros(N))

tunnel = np.array([[0,t1],
				   [0,0]])
cell = np.array([[0.0, t2],
				 [t2, 0]])


H = np.kron(np.eye(N),cell) + np.kron(T,tunnel) + np.transpose(np.kron(T,tunnel))

