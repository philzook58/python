#This program is beautiful

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

#Set grid points N and Length L gives step size a.
N = 200
L = 10.
a = L/N

# make source term a single point source in middle. Strength = 1/a^2?
j = np.zeros((N,N))
j[N/2,N/2] = 1/a/a
#dipole
#j[N/4,N/2] = 1/a/a
#j[3*N/4,N/2] = -1/a/a

#builds matrices of indices.
indices = np.indices((N, N))
i = indices[0]
k = indices[1]

#build the 2d laplacian vector in k-space
L2 = (2 * np.cos(2 * np.pi * i / N) + 2 * np.cos(2 * np.pi * k / N) - 4) / a / a
#i epsilon ?
#L2 = (2 * np.cos(2 * np.pi * i / N) + 2 * np.cos(2 *(1 + np.sign(k - N/2) * 15j) * np.pi * k / N) - 4) / a / a

#FFT magic
j_fft = np.fft.fft2(j)
phi_fft = j_fft / L2
phi_fft[0,0] = 0 # Removes divide by 0 constant at i=0 k=0

#Find Electric field by differentating in k-space
Ex_fft = phi_fft * 2j * np.sin(2 * np.pi * i / N) / a
Ey_fft = phi_fft * 2j * np.sin(2 * np.pi * k / N) / a

#return to real domain
phi = np.fft.ifft2(phi_fft)
Ex = np.fft.ifft2(Ex_fft)
Ey = np.fft.ifft2(Ey_fft)

#compare to ln(x)
x = np.linspace(0,L/2,N/2)
f = 1./ 2 / np.pi * ( np.log(2 * x/L) + np.log(2* (L-x) / L)  ) #constructing periodic solution of point sources
plt.plot(x,phi[N/2:,N/2], 'r', x, f,'b') #Not a great match


#bunch of plotting bull
#fig = plt.figure(figsize=plt.figaspect(2.))

#ax = fig.add_subplot(2, 1, 2, projection='3d')
#ax.plot_surface(i,k,np.abs(phi),cmap=cm.coolwarm)

#ax = fig.add_subplot(2, 1, 1)
#ax.quiver(i,k,Ex,Ey)

plt.show()
