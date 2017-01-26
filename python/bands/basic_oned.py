import numpy as np

import scipy as sp
from scipy import linalg as spLA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from numpy import linalg as LA
from matplotlib.ticker import LinearLocator, FormatStrFormatter

N = 100

t = 1.0


C =np.roll(np.eye(N),1,axis=0) # circulant off diagonal matrices
CT = np.transpose(C) 

temp = np.zeros(N)
temp[1] = 1.0
T = spLA.toeplitz(temp, np.zeros(N))

tunnel = np.array([[t]])
cell = np.array([[0.0]])




H = np.kron(np.eye(N),cell) + np.kron(T,tunnel) + np.transpose(np.kron(T,tunnel))

#energy = LA.eigvals(H)
# eigh may be faster but I may want to add dissipation or leads.

energies, wavefunctions = LA.eig(H)
# second index on wavefunction selects eigenvalue. First selects position
# I may want to smooth by convolving on something?


# interesting problem. Plots come out wrong unless fftshift. pyplot expects things in order
a = 1.0
ks = np.fft.fftshift(np.fft.fftfreq(N,d=a))
print ks
print energies
es = np.arange(2*min(energies), 2*max(energies), 0.1)
K, E = np.meshgrid(ks, es)
wavefunctions_k = np.fft.fftshift(np.fft.fft(wavefunctions,axis=0), axes=(0,))
#rho = np.fft.fftshift(rho, axis = 1)
rho_kk = np.abs(wavefunctions_k) ** 2
print "yes"
def smoothing(e,E):
	#e2 = np.outer(e, np.ones(E.shape))
	#E2= np.outer(np.ones(e.shape),E)
	return 1./((e-E)**2 + 0.1)

#rho_kk = np.fft.fft(rho_kk, axis=1)
#rho = sum( E * np.sum(smoothing(e,E)  rho_kk, axis=
#print "yo"
#map(lambda i:  smoothing rho_kk[i,:]  ,range(len(energies)))
#rho = np.einsum("ik,iyz",rho_kk, smoothing(energies,E))
#print "so"
#rho = np.diagonal(rho, axis1=0, axis2=1)
rho = np.zeros(E.shape)

#for i in range(len(ks)):
for j in range(len(es)):
	e = es[j]

	rho[j,:] = np.einsum("j,kj" , smoothing(energies,e) , rho_kk)



#plt.plot(rho[:,1])
#plt.plot(rho[:,10])
'''
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(K, E, rho,  cmap=cm.coolwarm)
ax.set_zlim(0, 1000)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))


'''

#plt.hist(energies, N/10)
plt.pcolormesh(K, E, rho)
#plt.contourf(K, E, rho)
plt.show()