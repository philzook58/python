import numpy as np
from scipy import integrate
from scipy import interpolate
from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt


N=100
v = .5

t = np.linspace(0,50,N)
x = t * v
y = np.zeros(N)
z = np.zeros(N)

#find splines
xs = UnivariateSpline(t, x, s=1)
ys = UnivariateSpline(t, y, s=1)
zs = UnivariateSpline(t, z, s=1)

dxdt = xs.derivative()(t)
dydt = ys.derivative()(t)
dzdt = zs.derivative()(t)

gamma = np.sqrt(1 - dxdt**2 - dydt**2 - dzdt**2)

tau = integrate.cumtrapz(gamma, t)
tau = np.insert(tau,0,0.)

plt.figure()
plt.plot(t,tau)
plt.figure()
plt.plot(t,x)
plt.show()
