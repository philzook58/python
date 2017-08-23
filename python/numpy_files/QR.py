#Note: This is a very bad implementation of the QR algorithm. For funzies only.

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import scipy.linalg as linalg

a = np.array([
    [2,-1,0 ],
    [-1,2,-1],
    [0,-1,2 ]])

print linalg.eigvals(a)


H,Q = linalg.hessenberg(a, calc_q=True)
print H
print Q
a = H

N = 50
result = np.zeros(N)

for i in range(N):
    Q,R = linalg.qr(a)
    #print "Q" + str(i) + ":"
    #print  Q
    #print "R" + str(i) + ":"
    #print R
    result[i]= R[0,0]
    a = np.dot(R,Q)
print "Q" + str(i) + ":"
print  Q
print "R" + str(i) + ":"
print R

plt.plot(result)
plt.show()
#exponential decay to ultimate value. Good after 5 iterations or so.
