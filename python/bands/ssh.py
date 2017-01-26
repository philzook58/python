import numpy as np

import scipy as sp
from scipy import linalg as spLA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from numpy import linalg as LA
from matplotlib.ticker import LinearLocator, FormatStrFormatter

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


energies, wavefunctions = LA.eig(H)

a = 1.0
ks = np.fft.fftshift(np.fft.fftfreq(bands*N,d=a))

es = np.arange(2*min(energies), 2*max(energies), 0.1)
K, E = np.meshgrid(ks, es)
wavefunctions_k = np.fft.fftshift(np.fft.fft(wavefunctions,axis=0), axes=(0,))

rho_kk = np.abs(wavefunctions_k) ** 2

def smoothing(e,E):
	return 1./((e-E)**2 + 0.1)
print E.shape
rho = np.zeros( E.shape )
print energies.shape

for j in range(len(es)):
	e = es[j]

	rho[j,:] = np.einsum("j,kj" , smoothing(energies,e) , rho_kk)


def compressbrillouin(rho, axis=1):
	n = rho.shape[axis]
	return rho[:,:n/2] + rho[:,n/2:]

#plt.pcolormesh(K, E, rho)
print energies
plt.plot(abs(wavefunctions[:,22])**2)
plt.show()