import numpy as np
from scipy.fftpack import fft2, ifft2

N = 100
L=10.
dx = L/N
x = np.linspace(0,L,N,endpoint=False)
y = np.linspace(0,L,N,endpoint=False)
xv, yv = np.meshgrid(x,y)

dk = 2 * np.pi / L
kx = np.linspace(0,2 * np.pi / dx,N,endpoint=False)
ky = np.linspace(0,2 * np.pi / dx,N,endpoint=False)
kxv, kyv = np.meshgrid(kx,ky)

#Forward and backard differences in x and y directions given in k space.
Dfx = (np.exp(1.j * kxv * dx) - 1)/dx
Dfy = (np.exp(1.j * kyv * dx) - 1)/dx
Dbx = (1 - np.exp(-1.j * kxv * dx))/dx
Dby = (1 - np.exp(-1.j * kyv * dx))/dx
# k-space laplacian
L2 = (4 - np.exp(1.j * kxv * dx) - np.exp(-1.j * kxv * dx) - np.exp(1.j * kyv * dx) - np.exp(-1.j * kyv * dx) ) / dx**2
L2[0,0] = 1 #freaks out at k=0

# associated with the up and right edge coming out of vertex. There are two edges per vertex on square graph
Ax  = np.zeros((N,N))
Ay  = np.zeros((N,N))

def pos(x):
    return int(N * x/L)

#face sources and vertex sources
#By picking sources we may pick vortex (curly face) or charge (divergency vertex) sources
sourcef = np.zeros((N,N))
sourcef[pos(L/2 + .1),pos(L/2)] = -1/dx**2
#sourcef[pos(L/2 - .1),pos(L/2)] = 1/dx**2

sourcev = np.zeros((N,N))

#make charges
'''
sourcev = sourcef
sourcef = np.zeros((N,N))
'''

# face and vertex potentials
phikf = fft2(sourcef) / L2
phikf[0,:]=0
phikf[:,0]=0

phikv = fft2(sourcev) / L2
phikv[0,:]=0
phikv[:,0]=0

phiv= np.real(ifft2(phikv))
phif= np.real(ifft2(phikf))

# A = curl phif + grad phiv is a 2D helmholtz decomposition
# curl uses backards difference, grad uses forward difference. It's how it works out
# curl: face -> edge is the transpose of curl: edge -> face and takes backwards to forwards difference
Akx = Dby * phikf + Dfx * phikv
Aky = - Dbx * phikf + Dfy * phikv

Ax = np.real(ifft2(Akx))
Ay = np.real(ifft2(Aky))


# duality
# It's like doing a line integral in k space.
psikv = Akx/Dfx + Aky/Dfy
psikv[0,:] = 0
psikv[:,0] = 0

psiv = np.real(ifft2(psikv))



import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()

#plot vector field
Q = plt.quiver(xv, yv, Ax, Ay, units='width')

#plot potential
'''
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(xv,yv,phif)
'''

#plot dual potential


ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(xv,yv,psiv)


'''
ax = fig.add_subplot(121, projection='3d')
ax.plot_surface(xv,yv,phif)
ax = fig.add_subplot(122, projection='3d')
ax.plot_surface(xv,yv,np.imag(ifft2(phikf)))
'''

'''
ax = fig.add_subplot(121, projection='3d')
ax.plot_surface(xv,yv,Ax)

ax = fig.add_subplot(122, projection='3d')
ax.plot_surface(xv,yv,Ay)
'''
plt.show()
