
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

from scipy import signal

T = 1000.
N = 1000
initcond = pack(1. + 0.j ,0. + 1.j)
t = np.linspace(0,T, N)

sol = odeint(diffeq, initcond, t)

f , P = signal.periodogram(sol[:,1],N/T)
plt.plot(t,sol[:,1])
plt.figure()
plt.plot(f,P)
plt.show()
