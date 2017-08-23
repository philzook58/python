
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import scipy.integrate as integrate


k = 1 # spring constant
b = .1 # nonlinear term
drag = .1 # drag coefficient
F = 1
scanrate = .01
tnum = 10000
fend = 3
tend = fend/scanrate
averagenum = 500

def freq(t):
    return t * scanrate

d=np.zeros(2)
def deriv(y, t):

    pos = y[0]
    vel = y[1]
    d[0] = vel
    d[1]= -k * pos + b * pos * pos - drag * vel + F * np.cos(freq(t) * t)
    return d

y0 = np.zeros(2)
y0[0] = 1
y0[1] = 1


t = np.linspace(0, tend, tnum)
y0 = np.ravel(y0)

sol = integrate.odeint(deriv, y0, t)
sample = np.reshape(sol[:,0], (tnum/averagenum, averagenum))
freqs = freq(np.reshape(t, (tnum/averagenum, averagenum)))[:,0]
newsample = np.amax(np.abs(sample), axis=1)
print newsample

#np.amax(np.abs(sol[:]))
plt.plot(freqs,newsample)
plt.show()
