'''

Author: Alex Baker
Date : 3 April 2008
Description : Investigate the properties of the Pauli Spin matricies.

'''

import numpy as np
import numpy.linalg as la

# pauli spin

sx = np.array([[0, 1],[ 1, 0]])
sy = np.array([[0, -1j],[1j, 0]])
sz = np.array([[1, 0],[0, -1]])

# sigma functions

sigma_x = np.array([[0, 1],[1, 0]])
sigma_y = np.array([[0, -1j],[1j, 0]])
sigma_z = np.array([[1, 0],[0, -1]])

# standard basis

spin_up = np.array([[1],[0]])
spin_down = np.array([[0],[1]])

# spin ladder operators

sigma_one_plus = sigma_x + 1j * sigma_y
sigma_two_plus = sigma_x + 1j * sigma_y

print 'example 1\n========='
print 's_{z} |+1/2, +1/2> = frac{hbar}{2} ( sigma_{1z} tensor 1_{2} + 1_{1} tensor sigma_{2z} ) |+1/2, +1/2>'
print np.mat(np.kron(sigma_z, identity(2))) * np.mat(np.kron(spin_up, spin_up))

print 'example 2\n========='
print 's_{+} |-1/2, -1/2>'
print (np.mat(np.kron(sigma_one_plus, identity(2))) * np.mat(np.kron(spin_down, spin_down)) + np.mat(np.kron(identity(2), sigma_one_plus)) * mat(kron(spin_down, spin_down))) / 2

print 'example 3\n========='
print 's_{+} |+1/2, -1/2>'
print (np.mat(np.kron(sigma_one_plus, identity(2))) * mat(kron(spin_up, spin_down)) + mat(kron(identity(2), sigma_one_plus)) * mat(kron(spin_up, spin_down))) / 2

print 'example 4\n========='
print 's_{+} |-1/2, +1/2>'
print (mat(kron(sigma_one_plus, identity(2))) * mat(kron(spin_down, spin_up)) + mat(kron(identity(2), sigma_one_plus)) * mat(kron(spin_down, spin_up))) / 2
