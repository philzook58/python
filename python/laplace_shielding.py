import numpy as np
from scipy.fftpack import fft2, ifft2

N = 50
L=1.
dx = L/N
x = np.linspace(0,L,N,endpoint=False)
y = np.linspace(0,L,N,endpoint=False)
xv, yv = np.meshgrid(x,y)

dk = 2 * np.pi / L
kx = np.linspace(0,2 * np.pi / dx,N,endpoint=False)
ky = np.linspace(0,2 * np.pi / dx,N,endpoint=False)
kxv, kyv = np.meshgrid(kx,ky)

phi  = np.zeros((N,N))

def pos(x):
    return int(N * x/L)



source = np.zeros((N,N))
#source[pos(.4),pos(.5)] = -1/dx**2
source[0,0] = -1/dx**2
#source[pos(.6),0] = 1/dx**2
L2 = (4 - np.exp(1.j * kxv * dx) - np.exp(-1.j * kxv * dx) - np.exp(1.j * kyv * dx) - np.exp(-1.j * kyv * dx) ) / dx**2
#L2[0,0] = 1 #freaks out at k=0
m = 1. / L/2
L2 = L2 + m**2
phik = fft2(source) / L2
phik[0,0]=0
phi = np.real(ifft2(phik))


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
'''
ax = fig.add_subplot(121, projection='3d')
ax.plot_surface(xv,yv,source)

ax = fig.add_subplot(122, projection='3d')
ax.plot_surface(xv,yv,phi)'''

ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(xv,yv,phi)
ax.plot_surface(xv,yv,np.exp(-1/L* np.sqrt(xv**2+yv**2)) * 1/4./np.pi * np.log(xv**2 + yv**2))
plt.show()
