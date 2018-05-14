




F = - sin(theta)
dx =


Q = SemiDefinite(2) 
Q2 = SemiDefinite(2) 

# V = x Q x > 0
# Vdot = x Q xdot + xdot Q x = x Q' x < 0
# => one constraint for every power of x (2n constraints). xs that can't be achieved have to be zero

a = [1,0,0,4] # set of coefficients xdot = 1 + 4 x^3
constraints = []
# This is inelgant but at least it's striaghtforward
for power in range(2*n):
	#convolution for Q'
	constraintL = 0
	#for i in range(n):
		for j in range(n):
		  #if i + j == power:
		  i = j - power
		  if i < n:
		  	constraintL = constraintL + Q2[power - j, j]

	constraintR = 0
	for i in range(n):
		for j in range(n):
			for k in range(len(a)):
				if i + j + k == power:
					contraintR = constraintR + j * Q[i, j] * a[k] + i * Q[i, j] * a[k]
    constraints.append(contraintR == constraintL)




