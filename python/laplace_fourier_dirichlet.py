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

# will essentially put the thing in a box of size L/2
def sinify(v):
    v[:,::2]=0. #destroy even elements
    v[::2,:]=0.
    return 1.j * np.imag(v)





source = np.zeros((N,N))
source[pos(.24),pos(.24)] = -1/dx**2
#source[pos(.6),0] = 1/dx**2
L2 = (4 - np.exp(1.j * kxv * dx) - np.exp(-1.j * kxv * dx) - np.exp(1.j * kyv * dx) - np.exp(-1.j * kyv * dx) ) / dx**2
L2[0,0] = 1 #freaks out at k=0
phik = fft2(source) / L2
phik[0,0]=0
phik = sinify(phik)
phi = np.real(ifft2(phik))


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(121, projection='3d')
ax.plot_surface(xv,yv,source)

ax = fig.add_subplot(122, projection='3d')
ax.plot_surface(xv,yv,phi)
plt.show()
