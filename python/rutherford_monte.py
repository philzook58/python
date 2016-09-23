import numpy as np
from scipy import integrate

z0 = -20.0
'''
class Orbit:
    def __init__(self, E=1.):
        initxy = np.random.randn(2)
        self.init = np.append(initxy,z0)
        self.x = self.init
        self.v = np.array([ 0, 0 ,np.sqrt(E)])
    def packstate(self,state):
        return np.flatten(state.x,state.v)
    def unpackstate(self,state):

    def solve(self):
        integrate.odeint

'''


def F(x):
    return .1 * x / np.linalg.norm(x)**1.5

def D(x,t):
    return np.concatenate((x[3:],F(x[0:3])))


samples = 100

E=.5

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')


t = np.linspace(0,50,100)

def update(E):
    ax.set_title('E='+str(E))
    print E
    for i in range(samples):
        initxy = 5*np.random.randn(2)
        init = np.append(initxy,[z0, 0., 0., np.sqrt(E)])
        sol = integrate.odeint(D, init, t)
        ax.plot(sol[:,0], sol[:,1],sol[:,2])

update(E)
'''
from matplotlib.widgets import Slider
axE = plt.axes([0.25, 0.1, 0.65, 0.03],)
sE = Slider(axE, 'E', 0.1, 10.0, valinit=1.)

def updateslide(val):
    E = sE.val
    ax.cla()
    update(E)
sE.on_changed(updateslide)
'''

plt.show()
