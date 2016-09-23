
#A suggesiton for the classical fractional hall effect
#Is a mean field organiztion of the cycltron phases, such that they synchronize.
#Leading to an effective time and angle dependant
# self consistantly dz/dt2 = i w dz/dt + P
# where E is a vortex configuration by conjecture. P = f(|z|)z^n
#  and also has angular time dependance z/|z|

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


omega =1.
g = .5

B = -1.

#Lagrangian L = r^2 thetadot^2 + rdot^2 + r^2 B thetadot
n = 2
#potential = r^2 (cos(n theta) + 1)
def diffeq(x,t):

    theta = x[0]
    thetadot = x[1]
    r = x[2]
    rdot = x[3]

    accel = np.zeros(4)
    accel[0]= thetadot
    accel[1]= -2. * (B * rdot + rdot * thetadot ) / r + g * np.sin(n * theta)
    accel[2]= rdot
    accel[3] = 2. * r * B * thetadot + r * thetadot**2 - 2. *g *  r *(np.cos(n* theta)+1)

    return accel

from scipy import signal

T = 100.
N = 1000
initcond = np.array([0.,2.,1.,0.])
t = np.linspace(0,T, N)

sol = odeint(diffeq, initcond, t)

#f , P = signal.periodogram(sol[:,1],N/T)
plt.plot(t,sol[:,2]*np.cos(sol[:,0]))
plt.plot(t,sol[:,2]*np.sin(sol[:,0]))
#plt.figure()
#plt.plot(f,P)
plt.show()
