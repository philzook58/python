import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

N = 6

hbar = 1.
m = 1.
w = 1.


E = np.diag((np.arange(N) + .5) * hbar * w)
a = np.roll(np.sqrt(np.diag(np.arange(N))), -1, axis=0)
adag = np.transpose(a)
print a
print np.dot(adag,a)
x = (a + adag) * np.sqrt(hbar / 2 / m / w)
p = 1.j * (adag - a) * np.sqrt(hbar * m * w / 2)

H0 =  m * w * w /2 * np.dot(x,x) + np.dot(p,p)/2 / m

H1 = 0.1 * np.dot(np.dot(x,x),x)
print la.eigvalsh(H0)
print la.eigvalsh(H0+H1)

M=20
gs = np.linspace(0,1,M)
levels = np.zeros((M,N))
for m in range(M):
    levels[m,:]  = la.eigvalsh(H0 + gs[m]*H1)
for n in range(N):
    plt.plot(gs,levels[:,n])
plt.show()
