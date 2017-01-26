import numpy as np

import scipy as sp
from scipy import linalg as spLA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from numpy import linalg as LA
from matplotlib.ticker import LinearLocator, FormatStrFormatter

N = 50

t1 = 1.0
t2 = -0.5
t3 = -.5
bands = 2

C =np.roll(np.eye(N),1,axis=0) # circulant off diagonal matrices
CT = np.transpose(C) 

temp = np.zeros(N)
temp[1] = 1.0
T = spLA.toeplitz(temp, np.zeros(N))

tunnel = np.array([[0,t1],
				   [0,0]])

def H(k):
	cell = np.array([[t3*np.sin(k) , t2],
				 [t2, -t3 * np.sin(k)]])

	return np.kron(np.eye(N),cell) + np.kron(T,tunnel) + np.transpose(np.kron(T,tunnel))





numk = 300

ks = np.linspace(-1 * np.pi ,1 * np.pi ,numk)
E = np.zeros((numk, N*bands))
for nk in range(numk):
	k = ks[nk]
	E[nk, :] = np.sort(LA.eigvals(H(k)))



plt.plot(ks, E)
plt.show()
