#I should try to see frequency fractionalization in nonlinear systems
# scan parametric oscillator
# response only?


import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import scipy.integrate as integrate


N = 5

B = 1

def deriv(y, t):
    y = np.reshape(y , (N,2,2))
    pos = y[:,:,0]
    vel = y[:,:,1]
    d = np.zeros((N,2,2))
    d[:,:,0]=vel
    d[:,:,1]= -1 * pos +
    return np.ravel(d)

y0 = np.zeros((N,2,2))
y0[0,0,0] = 1
y0[0,1,0] = 1

tnum = 100
t = np.linspace(0, 5, tnum)
y0 = np.ravel(y0)

sol = integrate.odeint(deriv, y0, t)
sol = np.reshape(sol , (tnum,N,2,2))
print sol[:,0,:,1]
#plt.plot(t,sol[:,0,0,0])
#plt.show()


from  matplotlib.animation import FuncAnimation

# Create new Figure and an Axes which fills it.
fig = plt.figure(figsize=(7,7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
xmin = np.amin(sol[:,:,0,0])
ymin = np.amin(sol[:,:,1,0])
xmax = np.amax(sol[:,:,0,0])
ymax = np.amax(sol[:,:,1,0])


ax.set_xlim(xmin,xmax), ax.set_xticks([])
ax.set_ylim(ymin,ymax), ax.set_yticks([])

scat = ax.scatter(sol[0,:,0,0], sol[0,:,1,0])


def update(frame_number):
    #current_index = frame_number % n_drops
    time = frame_number % tnum
    scat.set_offsets(sol[time, :,:,0])

animation = FuncAnimation(fig, update, interval=100)
plt.show()
