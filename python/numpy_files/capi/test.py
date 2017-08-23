import numpy as np
import array_square


a = np.array([6.4 + 14.0j,24,3],dtype=np.complex64)
print a
b = array_square.square_func_np(a)
print b