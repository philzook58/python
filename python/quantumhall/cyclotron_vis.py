
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


def pack(z,zdot):
    return np.array([np.real(z),np.imag(z),np.real(zdot),np.imag(zdot)])

def unpack(x):
    return x[0]+1.j * x[1], x[2]+1.j * x[3],

def accel(z,zdot):
    return 1.j * omega * zdot + g * np.conj(z)**3

def diffeq(x,t):
    z, zdot = unpack(x)
    return pack(zdot, accel(z,zdot))


ball = sphere(pos=[1,0,0],  radius=0.1)
center = sphere(pos=[0,0,0],  radius=0.1)

initcond = pack(1. + 0.j ,0. + 1.j)
t = np.array([0,0.01])

while 1:
    rate(100)
    sol = odeint(diffeq, initcond, t)
    x = sol[-1,0]
    y = sol[-1,1]
    initcond=sol[-1,:]
    ball.pos = [x,y,0]
