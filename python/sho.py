import numpy as np
from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt

N = 100
L=2.
dt = L/N
w02 = 4. # omega_0 ^ 2. oscillation constant
t = np.linspace(0,L,N,endpoint=False)

def pos(x):
    return int(N * x/L)

dw = 2 * np.pi / L
epsilon =  dw/2
w = np.linspace(0,2 * np.pi / dt,N,endpoint=False)

L2 = (2 - np.exp(1.j * w * dt) - np.exp(-1.j * w * dt)  ) / (dt**2) - w02 # + 1.j* dw**2 
print L2
L2[0]=1.j*dw
source = np.zeros(N)
source[pos(.5*L)] = -1/dt**2

phik = fft(source) / L2
#print phik
#phik[0]=0
phi = np.real(ifft(phik))
phii = np.imag(ifft(phik))
print phi

plt.plot(t, phi)
plt.plot(t, phii)
plt.show()
