import numpy as np
import matplotlib.pyplot as plt

N=10

#Now it is setup to plot filling factor style density

def Prob(x):
    prod = 1.
    for i in range(N):
        for j in range(i):
            prod = prod * ((x[i,0]-x[j,0])**2 + (x[i,1]-x[j,1])**2)**3
    return prod * np.exp(- 0.5 * np.sum(x * x))


def suggestMove(fromx):
    '''
    index = np.random.randint(N)
    newx = x
    newx = x[index] + random.randn()
    '''
    return np.random.randn(N,2) + x



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

q = np.sqrt(data[:,:,0]**2 + data[:,:,1]**2)
#r = np.linspace( 0.	201, 7., num = 128)
p,edges = np.histogram(q, bins=128,density=True)
edges = (edges[1:] + edges[:-1])/2

#Will get better sampling results if I move this radial factor into the probability.
#The origin is more poorly sampled just due to geometric factors. And then dividing
# by a small number amplifies this.
p = N * p / edges
#plt.hist(r,bins=128)
plt.plot(edges,p)
plt.show()
