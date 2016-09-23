from stl import mesh
from visual import *
import numpy as np
from PIL import Image # from PIL 
from PIL import ImageGrab # from PIL
import time

scene2 = display(title='Examples of Tetrahedrons',
     x=0, y=0, width=600, height=600,
     center=(5,0,0), background=(0,1,1))


your_mesh = mesh.Mesh.from_file('beth.stl')

print your_mesh.vectors.shape

triangles = np.reshape(your_mesh.vectors, (your_mesh.vectors.shape[0]*3,3))

f = frame()
tri = faces(
    pos = triangles,
    #color = [
    #    [1.,0.,0.], [0.5,0.5,0.], [0.,1.,0.], # first tri - colors
    #    [0.,0.,1.], [0.,0.5,0.5], [0.,1.,0.]  # second tri - colors
    #],
    color = color.red,
    normals = your_mesh.normals,
    frame = f,
    material = materials.plastic
)
tri.make_normals()
tri.make_twosided()
f.rotate(angle=60,axis = [.454,.674,.22353])
#time.sleep(1)

#while True:
#    rate(100)
 #   f.rotate(angle=0.01,axis = [.454,.674,.22353])
for i in range(100):
    rate(100)
    f.rotate(angle=0.01,axis = [.454,.674,.22353])
im = ImageGrab.grab((0,0,600,600)) # if window located at (0,0), width=height=600
im.save("beth.jpg")


