import numpy as np
from scipy import integrate
from scipy import interpolate
from scipy.interpolate import UnivariateSpline
from scipy import optimize

Bz = 1.
omega = 1.
Bw = .1

def B(t):
    return np.array([Bw * np.cos(omega*t),Bw * np.sin(omega*t),Bz])

def DSdt(S,t):
    return np.cross(  B(t)   , S   )

#t = np.linspace(0,10,100)
T = 1000
t = np.arange(0,T,.5)
init = np.array([0.,0.,1.])
sol = integrate.odeint(DSdt, init, t)


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.plot(sol[:,0], sol[:,1],sol[:,2])
plt.show()
