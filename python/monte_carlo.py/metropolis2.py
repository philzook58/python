import numpy as np
import matplotlib.pyplot as plt

N=5


def Prob(x):
    prod = 1.
    for i in range(N):
        for j in range(i):
            prod = prod * ((x[i,0]-x[j,0])**2 + (x[i,1]-x[j,1])**2)
    return prod * np.exp(- 0.5 * np.sum(x * x))


def suggestMove(fromx):
    '''
    index = np.random.randint(N)
    newx = x
    newx = x[index] + random.randn()
    '''
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


x = np.random.randn(N,2)
steps = 100000
data = np.zeros((steps,N,2))
for step in range(steps):
    x = Step(x)
    data[step,:,:] = x

r = np.sqrt(data[:,:,0]**2 + data[:,:,1]**2)
plt.hist(r,bins=128)
plt.show()
