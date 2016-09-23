import numpy as np
from numpy import kron
import scipy.linalg as la

# pauli spin

sx = np.matrix([[0, 1],[ 1, 0]])/2.
sy = np.matrix([[0, -1j],[1j, 0]])/2.
sz = np.matrix([[1, 0],[0, -1]])/2.

# sigma functions

sigma_x = np.matrix([[0, 1],[1, 0]])
sigma_y = np.matrix([[0, -1j],[1j, 0]])
sigma_z = np.matrix([[1, 0],[0, -1]])
I = np.identity(2)
#print I

# standard basis

spin_up = np.array([[1],[0]])
spin_down = np.array([[0],[1]])

# spin ladder operators

sigma_plus = (sigma_x + 1j * sigma_y)/2
sigma_minus = sigma_plus.H

#print sigma_minus

sigma_x2 = np.kron(sigma_x,sigma_x)
sigma_y2 = np.kron(sigma_y,sigma_y)
sigma_z2 = np.kron(sigma_z,sigma_z)

def krony(s,i,N):
    mat = np.array([1])
    for j in range(N):
        if j == i:
            mat = kron(mat,s)
        else:
            mat = kron(mat,I)
    return mat

def s(xyz,i,N):

    mat = np.array([1])
    for j in range(N):
        if j == i:
            mat = kron(mat,s)
        else:
            mat = kron(mat,I)
    return mat


print krony(sx,1,2)

sx1 = kron(sx,I)
sy1 = kron(sy,I)
sz1 = kron(sz,I)


sx2 = kron(I,sx)
sy2 = kron(I,sy)
sz2 = kron(I,sz)

S2 =  (sx1+sx2)**2 + (sy1+sy2)**2 + (sz1+sz2)**2
print (sz1+sz2)**2
print S2
print la.eigvalsh(S2)


sx = np.matrix([[0, 1],[ 1, 0]])/2.
sy = np.matrix([[0, -1j],[1j, 0]])/2.
sz = np.matrix([[1, 0],[0, -1]])/2.

def sx(i,N=2):
    return krony(np.matrix([[0, 1],[ 1, 0]])/2.,i,N)

#I need to cluster eigenvectors somehow.
#spin chain would be easy

#do odeint to solve.
#show somehow nice?

#print la.schur(S2)
