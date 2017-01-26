import numpy as np

import scipy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from numpy import linalg as LA



# automatic transofrmation between band and lattice would be nice.
# by assumption of toroidal geometry and uniformity, hamiltonian is circulant, given by convolution with a vector
#def unitCellH(cellpsi, neighborspsi):
def simpleCellH(coords, params): # params is dictionary of hamiltonian parameters, coords is displacement from unit cell
	#print coords.x
	H = np.zeros(1, dtype='complex')
	if coords['x'] == 1:
		H[0] += params['t']
	if coords['x'] == -1:
		H[0] += params['t'] 
	return H

def dimerCellH(coords, params): # params is dictionary of hamiltonian parameters, coords is displacement from unit cell
	#print coords.x
	H = np.zeros((2,2), dtype='complex')
	if coords['x'] == 1:
		H[1,1] += params['t']
	if coords['x'] == -1:
		H[0,0] += params['t'] 
	if coords['x'] == 0:
		H[0,1] += params['t'] 
		H[1,0] += params['t'] 

	return H



def kSpaceH(k, unitH):
	params = {'t' : 1.0}

	a = 1.0
	H = np.zeros((2,2),dtype='complex')
	for i in range(-1,2):
		coords = {'x':i}
		H += np.exp( 1.j * k * a) * unitH(coords, params)
	return H


ks = np.linspace(-1 * np.pi, 1 * np.pi, 100)
#energies = np.zeros(100)

#energies = np.vectorize( lambda k: LA.eigvals(kSpaceH(k, unitCellH)))(ks) # needat least two bands to use eigvalsh

#energies = np.vectorize( lambda k: kSpaceH(k, unitCellH),otypes=[np.float])(ks) 
energies = np.zeros((100,2),dtype='complex')
i = 0
for k in ks:
	energies[i,:]= LA.eigvals(kSpaceH(k, dimerCellH))
	i = i + 1



plt.plot(ks, energies)
plt.show()


