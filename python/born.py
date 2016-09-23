import numpy as np

# A first step, attempt to fourier trasnfrom 1/(q^2-E^2+i\epslion) in some manner

from scipy.integrate import quad


def G0(q, E, epsilon=0.1):
    return 1/(q**2 - E + 1.j*epsilon)

#firs step, fourier transfrom step function 1/

def FStep(q,E,epsilon=0.1):
    return 1/(q-E+1.j * epsilon)


def fourier(func,q,E,x):
    return np.exp(1.j * q * x) * func(q,E)




#print quad(lambda q: np.real(fourier(FStep,q,E,x)), -np.inf,np.inf)
#print quad(lambda q: np.imag(fourier(FStep,q,E,x)), -np.inf,np.inf)

def FTransform(func,x,E):
    return (quad(lambda q: np.real(fourier(func,q,E,x)), -np.inf,np.inf) ,quad(lambda q: np.imag(fourier(func,q,E,x)), -np.inf,np.inf))
for x in np.arange(10):
    print x
    print FTransform(FStep,x,0)
#np.vectorize
