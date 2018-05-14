import cvxpy as cvx
import numpy as np
import matplotlib.pyplot as plt

lookahead = 50
dt = 0.1
F = 1.0
objective = 0
A = np.array([[1,dt],[0,1]])
B = np.array([0,dt*F])
x0 = np.array([1,0])
xt = cvx.Variable(2)
state = [xt]
cost = 0
constraints = [xt == x0]
controls = []
for i in range(lookahead):
	ut = cvx.Variable()
	xtn = cvx.Variable(2)
	controls.append(ut)
	state.append(xtn)

	constraints.append(xtn == A*xt + B * ut )
	constraints.append(ut <= 1.0)   
	constraints.append(ut >= -1.0)  
	cost = cost + cvx.square(xtn[0]) #+ 0.1 * cvx.square(ut)

	xt = xtn

objective = cvx.Minimize(cost)
prob = cvx.Problem(objective, constraints)
sol = prob.solve(verbose=True)
print(sol)
pos = np.array(list(map( lambda x: x.value, state)))
us = np.array(list(map( lambda x: x.value, controls)))

plt.plot(pos[:,0,0])
plt.plot(us)
print(pos[:,0,0])
plt.show()
