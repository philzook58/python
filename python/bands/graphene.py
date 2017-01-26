import numpy as np

import scipy as sp
from scipy import linalg as spLA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from numpy import linalg as LA
from matplotlib.ticker import LinearLocator, FormatStrFormatter


def H(k):
	a1 = np.array([1,0])
	a2 = np.array([-1/2,np.sqrt(3)/2])
	a3 = np.array([-1/2,-np.sqrt(3)/2])

	kx = k[0]
	ky = k[1]
	t1 = 1.0
	t2 = 1.0
	ty = 1.0
	return np.array([ [0  ,          t2 + t1 * np.exp(1.j * np.dot(k,a2)) + t1 * np.exp(1.j * np.dot(k,a3))],
					  [t2 + t1 * np.exp(-1.j * np.dot(k,a2)) + t1 * np.exp(-1.j * np.dot(k,a3)),  0 ]  ])



N = 300

ks = np.linspace(-1 * np.pi ,1 * np.pi ,N)
KX, KY = np.meshgrid(ks, ks)

E1 = np.zeros(KX.shape)
E2 = np.zeros(KX.shape)

for nx in range(N):
	for ny in range(N):
		k = np.array([ks[nx],ks[ny]])
		energ = LA.eigvals(H(k))
		E1[nx,ny] =  min(energ)
		E2[nx,ny] = max(energ) 


fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(KX, KY, E1,  cmap=cm.coolwarm)
surf = ax.plot_surface(KX, KY, E2,  cmap=cm.coolwarm)
ax.set_zlim(-2, 2)
plt.show()