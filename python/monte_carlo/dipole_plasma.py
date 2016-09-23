import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

N=5

p = 1.
beta = 1.

def Prob(x):
    Energy = 0.
    for i in range(N):
        for j in range(i):
            dx = x[i,0] - x[j,0] + p * (np.cos(x[i,2]) - np.cos(x[j,2]))
            dy = x[i,1] - x[j,1] + p * (np.sin(x[i,2]) - np.sin(x[j,2]))
            Energy = Energy + np.log(dx**2 + dy**2)
    return np.exp(beta * Energy - 0.5 * np.sum(x * x))


def suggestMove(fromx):
    '''
    index = np.random.randint(N)
    newx = x
    newx = x[index] + random.randn()
    '''
    sugg = np.zeros(fromx.shape)
    sugg[:,:2]= np.random.randn(N,2) + fromx[:,:2]
    sugg[:,2]= np.random.random() * 2 * np.pi
    return sugg

#Maybe I want the other r?
def analyze(x):
    data = np.zeros((N*(N-1)/2,2))
    for i in range(N):
        for j in range(i):
            dx = x[i,0] - x[j,0] + p * (np.cos(x[i,2]) - np.cos(x[j,2]))
            dy = x[i,1] - x[j,1] + p * (np.sin(x[i,2]) - np.sin(x[j,2]))

            dx = x[i,0] - x[j,0]
            dy = x[i,1] - x[j,1] 

            r = np.sqrt(dx**2+dy**2)
            data[i*(i-1)/2+j,0] = r
            dangle2 = (x[i,2]-x[j,2])**2
            data[i*(i-1)/2+j, 1] = r
    return data





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



x = np.random.randn(N,3)
steps = 10000

data = np.zeros((steps,N*(N-1)/2,2))
for step in range(steps):
    x = Step(x)
    data[step,:,:] = analyze(x)

p,xedges, yedges = np.histogram2d(data[:,:,0].flatten(),data[:,:,1].flatten(), bins=128)
print np.sum(p)*(xedges[1]-xedges[0]) *(yedges[1]-yedges[0])
xedges = (xedges[1:] +xedges[:-1])/2
yedges = (yedges[1:] +yedges[:-1])/2
X, Y = np.meshgrid(xedges, yedges)

#Will get better sampling results if I move this radial factor into the probability.
#The origin is more poorly sampled just due to geometric factors. And then dividing
# by a small number amplifies this.
#p = N * p / edges

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, p, rstride=1, cstride=1, cmap='hsv',#facecolors=colors,
                       linewidth=0, antialiased=False)
#plt.hist(r,bins=128)
#plt.plot(edges,p)
plt.show()
