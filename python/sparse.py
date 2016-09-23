from scipy import sparse
from scipy.sparse import linalg as la
import numpy as np


N = 100
L = 1.
dx = L/N
dx2 = dx**2
K1 = sparse.diags([1./dx2, -2/dx2, 1/dx2], [-1, 0, 1], shape=(N, N))
I = sparse.identity(N, format='dia')
K2 = sparse.kron(K1,I)+sparse.kron(I,K1)

print K2.get_shape()

row  = np.array([N/2])
col  = np.array([0])
data = np.array([1/dx])
delta = sparse.coo_matrix((data, (row, col)), shape=(N,1)).tocsr()

print delta
source = sparse.kron(delta,delta)
print source.get_shape()
print source

phi = la.spsolve(K2, source)
phi = phi.reshape((N,N))


x = np.linspace(0,L,N,endpoint=False)
y = np.linspace(0,L,N,endpoint=False)
xv, yv = np.meshgrid(x,y)


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.plot_surface(xv,yv,source.toarray().reshape((N,N)))

ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(xv,yv,phi)

#plt.plot(x, phi[N/2,:])
plt.show()
