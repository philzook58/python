import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

N=5



def Prob(x):
    prod = 1.
    for i in range(N):
        for j in range(i):
            prod = prod * (x[i]-x[j])**2
    return prod * np.exp(- 0.5 * np.sum(x * x))

def Energy(field):
	

def suggestMove(fromx):

    index = np.random.randint(N,size=2)
    newx = x
    newx = x[index] + random.randn()
    return np.random.randn(N) + x



def Step(x):
    xnew = suggestMove(x)
    xold = x
    acceptanceratio = Prob(xnew)/Prob(xold)
    if acceptanceratio > 1:
        xnew = xnew
    else:
        if np.random.rand() < acceptanceratio:
            xnew = xnew
        else:
            xnew = xold
    return xnew

def Gather(field):
	E = 
	E2 = E**2
	M = np.sum(field)
	M2 = M**2
	return np.array([E,E2, M, M2])


field = np.ones((N,N))
steps = 1000000
numinfo = 4 #E, E**2, M, M**2
data = np.zeros((steps,numinfo))
for step in range(steps):
    x = Step(x)
    data[step,:]= 

plt.hist(data,bins=128)
plt.show()