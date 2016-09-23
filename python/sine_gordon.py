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
source[pos(.4),0] = -20/dx**2
source[pos(.6),0] = 20/dx**2
L = (4 - np.exp(1.j * kxv * dx) - np.exp(-1.j * kxv * dx) - np.exp(1.j * kyv * dx) - np.exp(-1.j * kyv * dx) ) / dx**2
L[0,0] = 1 #freaks out at k=0

iters = 5
phik = fft2(source) / L
phik[0,0]=0
phi = np.real(ifft2(phik))
phi0 = np.copy(phi)

for i in range(iters):
    print i
    sourceeff = source - 100*np.sin(phi)
    phik = fft2(sourceeff) / L
    phik[0,0]=0
    phi = np.real(ifft2(phik))

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(221, projection='3d')
ax.plot_surface(xv,yv,source)

ax = fig.add_subplot(222, projection='3d')
ax.plot_surface(xv,yv,phi)
ax = fig.add_subplot(223, projection='3d')
ax.plot_surface(xv,yv,sourceeff)
'''
#print phi-phi0
plt.plot(x,phi0[:,0])
plt.plot(x,phi[:,0])
'''
plt.show()
