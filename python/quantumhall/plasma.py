import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from visual import *
from visual.controls import *

N=10
dt = 0.01

pos = np.random.randn(N,3)
vel = np.random.randn(N,3)
pos[:,2]=0
vel[:,2]=0
#sphere(pos=(0,0,0),  radius=0.5, color=color.cyan)
'''w = window(menus=False, title="VPython",
           x=0, y=0, width=600, height=600)
display(window=w, x=50, y=30, width=200, height=150)
'''
colors = [color.red, color.green, color.blue,
          color.yellow, color.cyan, color.magenta]

B = np.array([0,0,5])
ballz = []
for i in range(N):
    ballz.append(sphere(pos=pos[i,:],  radius=0.5, color=colors[i%6]))

w = 100
c = controls(x=0, y=0, width=w, height=w, range=60)
ctrl = slider(min=0., max = 10., value =1.)
#b = button( pos=(0,0), width=60, height=60,
#              text='Click me', action=lambda: change() )

#print dir(w)
print dir(scene.window.win)
while 1:
    B[2] = ctrl.value
    rate(100)
    pos = pos + dt * vel
    #np.einsum('Ni,Mj')
    F = np.zeros((N,N,3))
    for i in range(N):
        for j in range(N):
            if i != j:
                r = pos[i,:]- pos[j,:]
                F[i,j,:]= -r / np.sum(r**2)

    a = -pos + np.sum(F,axis = 0) + np.cross(vel,B)
    vel = vel + dt * a

    for i in range(N):
        ball = ballz[i]
        ball.pos = pos[i,:]
    #scene.window.win.Update()
