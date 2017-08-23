#This program is beautiful

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import scipy.linalg as linalg

#Set grid points N and Length L gives step size a.
N = 4
L = 10.
a = L/N

#np.meshgrid()
def matToCoord(a):
    return np.reshape(a, (N, N, N, N))

def coordToMat(a):
    return np.reshape(a, (N*N, N*N))

def vecToCoord(a):
    return np.reshape(a, (N, N))

def coordToVec(a):
    return np.reshape(a, (N*N))

x = np.linspace(0.,L, num=N)
y = np.linspace(0.,L, num=N)

xvec, yvec = np.meshgrid(x, y, sparse=False, indexing='xy')

Laplace = np.zeros((N,N,N,N))

for i in range(N):
    for j in range(N):
        x = i-1
        y = j-1
        Laplace[x-1,y,x,y] = -1
        Laplace[x,y-1,x,y] = -1
        Laplace[x+1,y,x,y] = -1
        Laplace[x,y+1,x,y] = -1
        Laplace[x,y,x,y] = 4

#Laplace = Laplace / (a*a)
Laplace = coordToMat(Laplace)
print Laplace
Green = linalg.inv(Laplace+.1)


#plt.show()
