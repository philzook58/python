
#A suggesiton for the classical fractional hall effect
#Is a mean field organiztion of the cycltron phases, such that they synchronize.
#Leading to an effective time and angle dependant
# self consistantly dz/dt2 = i w dz/dt + P
# where E is a vortex configuration by conjecture. P = f(|z|)z^n
#  and also has angular time dependance z/|z|

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from visual import *


omega =1.
g = -.5

B = -1.

#Lagrangian L = r^2 thetadot^2 + rdot^2 + r^2 B thetadot
def diffeq(x,t):

    theta = x[0]
    thetadot = x[1]
    r = x[2]
    rdot = x[3]

    accel = np.zeros(4)
    accel[0]= thetadot
    accel[1]= -2. * (B * rdot + rdot * thetadot ) / r
    accel[2]= rdot
    accel[3] = 2. * r * B * thetadot + r * thetadot**2

    return accel

from scipy import signal

T = 1000.
N = 1000
ball = sphere(pos=[1,0,0],  radius=0.1)
center = sphere(pos=[0,0,0],  radius=0.1)
initcond = np.array([0.,2.,.5,0.])
t = np.array([0,0.01])
while 1:
    rate(100)
    sol = odeint(diffeq, initcond, t)
    x = sol[-1,2] * np.cos(sol[-1,0])
    y = sol[-1,2] * np.sin(sol[-1,0])
    initcond=sol[-1,:]
    ball.pos = [x,y,0]
