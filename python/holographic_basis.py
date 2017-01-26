''' 
So I had an idea
That it might make sense to describe a basis entirely by its value on a sphere encircling the domain
wich is then iplicitly progpated by the wave equation.
You would pick a patch and a transverse momentum on the patch.
Wavelet-like
Could use 



Alternatively, One could associate a grid of points (or pherhaps a coarsened blob if possible) in the interior 
using the free space green's function

Or in the actual time domain

I just like the idea of describing a basis for the bulk in terms of how it feels on a asymptotic surface

Then reconsturcting a potential in terms of its scattering data might be very straightforward.

An intesnity form of the thing is not obvious

The condition number of the connection between the bulk states and the boundary defined states

'''
import numpy as np

k = 1

def G(x1,x2):
	r = np.norm( x1 - x2)  
	return np.exp(1.j * k * r)/ (4 * np.pi * r)

#convert between lattice basis sampling in bulk and basis sampling on boundary
# random uniform sampling? Would be easier than systematic. Would need to tesselate some weird polyhedra.

#If I'm using G1 as essentially my basis parametized by positions, then the inner porduct of two states is the convolution of GG
# evaluted at a1 a2.

