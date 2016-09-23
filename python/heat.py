import numpy as np
from scipy.fftpack import fft2, ifft2
from scipy import integrate

N = 20
L=1.
dx = L/N
x = np.linspace(0,L,N,endpoint=False)
y = np.linspace(0,L,N,endpoint=False)
xv, yv = np.meshgrid(x,y)

dk = 2 * np.pi / L
kx = np.linspace(0,2 * np.pi / dx,N,endpoint=False)
ky = np.linspace(0,2 * np.pi / dx,N,endpoint=False)
kxv, kyv = np.meshgrid(kx,ky)

phi  = np.zeros((N,N))

def pos(x):
    return int(N * x/L)

phi0 = np.zeros((N,N))
NT = 2
t = np.linspace(0.,1.,NT)

phi0[pos(.5),pos(.5)] = 1/dx**2
L2 = (4 - np.exp(1.j * kxv * dx) - np.exp(-1.j * kxv * dx) - np.exp(1.j * kyv * dx) - np.exp(-1.j * kyv * dx) ) / dx**2
#L2[0,0] = 1 #freaks out at k=0
L2diff = np.real(ifft2(L2)).flatten()


def D(phi,t):
    Lphik = -1. * fft2(phi.reshape((N,N))) * L2
    return np.real(ifft2(Lphik)).flatten()

def gradient(phi,t):
    return -1. * L2diff

def main():
    sol,metadata = integrate.odeint(D, phi0.flatten(), t, Dfun = gradient, full_output=True)
    print(metadata)
    sol = sol.reshape(NT,N,N)

    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure()
    ax = fig.add_subplot(121, projection='3d')
    ax.plot_surface(xv, yv, sol[0,:,:] )

    ax = fig.add_subplot(122, projection='3d')
    ax.plot_surface(xv, yv, sol[-1,:,:]  )
    plt.show()


if __name__ == "__main__":
    # execute only if run as a script
    main()
