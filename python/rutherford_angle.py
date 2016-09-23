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


samples = 1000

E=.5

import matplotlib.pyplot as plt

angles = np.zeros(samples)

def angle(x):
    return np.arccos(x[2]/np.linalg.norm(x))

def update(E):
    for i in range(samples):
        initxy = 5*np.random.randn(2)
        init = np.append(initxy,[z0, 0., 0., np.sqrt(E)])
        sol = integrate.odeint(D, init, [0.,50.])
        angles[i] = angle(sol[-1,3:]))

update(E)
#print angles
plt.hist(angles, 50)

plt.show()
