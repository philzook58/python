import numpy as np

import scipy as sp
from scipy import linalg as spLA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from numpy import linalg as LA
from matplotlib.ticker import LinearLocator, FormatStrFormatter


def H(k):
	kx = k[0]
	ky = k[1]
	return np.array([ [0, kx+1.j*ky],
					 [kx-1.j*ky, 0]])





ks = np.linspace(-1,1,100)
KX, KY = np.meshgrid(ks, ks)

E1 = np.zeros(KX.shape)
E2 = np.zeros(KX.shape)

for nx in range(100):
	for ny in range(100):
		energ = LA.eigvals(H([ks[nx],ks[ny]]))
		E1[nx,ny] =  min(energ)
		E2[nx,ny] = max(energ) 


fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(KX, KY, E1,  cmap=cm.coolwarm)
surf = ax.plot_surface(KX, KY, E2,  cmap=cm.coolwarm)
ax.set_zlim(-2, 2)
plt.show()