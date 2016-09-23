import numpy as np
from scipy import integrate
from scipy import interpolate
from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt
from scipy import optimize



N=10
v = .5

tau = np.linspace(0,5,N)
t = tau / np.sqrt(1 - v**2)
x = t * v
y = np.zeros(N)
z = np.zeros(N)

ts = UnivariateSpline(tau, t, s=1)
xs = UnivariateSpline(tau, x, s=1)
ys = UnivariateSpline(tau, y, s=1)
zs = UnivariateSpline(tau, z, s=1)

xts = UnivariateSpline(t, x, s=1)
yts = UnivariateSpline(t, y, s=1)
zts = UnivariateSpline(t, z, s=1)

fieldx = 1.
fieldy = 0
fieldz = 0
fieldt = 2.

fieldr = np.array([fieldx,fieldy,fieldz])

def properinterval(tau,x,y,z,t):
    return (t-ts(tau))**2 - (x-xs(tau))**2 - (y-ys(tau))**2 - (z-zs(tau))**2

def EB(r, rs, v, a):
    gamma = 1/np.sqrt(1-np.norm(v)**2)
    R = np.linalg.norm(r-rs)
    n = (r-rs)/R
    firstterm = (n-v)/(gamma**2 * (1-np.dot(n,v))**3 * R**2)
    secondterm =  np.cross(n, np.cross(n - v, a)    ) /  (1-np.dot(n,v))**3 / R
    E = firstterm + secondterm
    B = np.cross(n,E)
    return {'E': E, 'B', B}

times = np.linspace(0,100,1000)

tauguess = 0.
for time in times:
    sol = optimize.root(properinterval, tauguess,args=(fieldx,fieldy,fieldz,time))
    soltau = sol.x
    tauguess = soltau
    rRet = np.array([xs(tau),ys(tau),zs(tau)])
    #dtdtau = ts.derivative()(tau)
    #v = np.array([xs.derivative()(tau),ys.derivative()(tau),zs.derivative()(tau)     ]) / dtdtau
    v = np.array([xts.derivative()(time),yts.derivative()(time) ,zts.derivative()(time)])
    a = np.array([xts.derivative(2)(time),yts.derivative(2)(time) ,zts.derivative(2)(time)])
    myEB = EB(fieldr,rRet,v, a)
    E = myEB.E
    B = myEB.B
    S = np.cross(E,B)




print soltau

#for light, x=t x =-t
plt.plot(t,t+fieldx-fieldt)
plt.plot(t,-t-fieldx+fieldt)
plt.show()
