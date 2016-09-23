import numpy as np
from scipy.fftpack import fft2, ifft2

N = 50
L=1.
dx = L/N
x = np.linspace(0,L,N,endpoint=False)
y = np.linspace(0,L,N,endpoint=False)
xv, yv = np.meshgrid(x,y)

# We can make y be time.
# epsilon is the rotation paramter

#Should make into notebook file, because i'm not sure what's going on
#putting into L2 does not work well
#lots of rough oscillations or noise
# Try forcing e^-rt * f as a solution. Or rather periodic e^-rt? Does not change anythin
#

dk = 2 * np.pi / L
epsilon =  dk/2
kx = np.linspace(0,2 * np.pi / dx,N,endpoint=False)
#ky = np.linspace(0,6 * np.pi / dx,N,endpoint=False) * 1.j - epsilon
ky = np.linspace(0,6 * np.pi / dx,N,endpoint=False)
kxv, kyv = np.meshgrid(kx,ky)

phi  = np.zeros((N,N))

def pos(x):
    return int(N * x/L)

source = np.zeros((N,N))
source[pos(.5),pos(.5)] = -1/dx**2
#source[pos(.6),0] = 1/dx**2
#L2 = (4 - np.exp(1.j * kxv * dx) - np.exp(-1.j * kxv * dx) - np.exp(1.j * kyv * dx) - np.exp(-1.j * kyv * dx)) / dx**2
#L2 = (np.exp(1.j * kxv * dx) - np.exp(-1.j * kxv * dx) - np.exp(1.j * kyv * dx) + np.exp(-1.j * kyv * dx) + 1.j * epsilon  + 1) / dx**2
L2 = (np.cos(kxv * dx) - np.cos(kyv * dx) ) / dx**2  - epsilon * (np.exp(1.j* kyv * dx) - 1)/dx
#L2[0,0] = 1 #freaks out at k=0
phik = fft2(source) / L2
phik[0,0]=0
phi = np.real(ifft2(phik))


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(121, projection='3d')
ax.plot_surface(xv,yv,source)

ax = fig.add_subplot(122, projection='3d')
ax.plot_surface(xv,yv,phi)
plt.show()
