from meshpy.triangle import MeshInfo, build, refine
import numpy as np

mesh_info = MeshInfo()
mesh_info.set_points([
    (0,0),
    (0,1),
    (1,1),
    (1,0)
    ])
mesh_info.set_facets([
    [0,1],
    [1,2],
    [2,3],
    [3,0]



    ])

def refinement_func(tri_points, area):
    max_area=0.001
    return bool(area>max_area);

mesh = build(mesh_info, refinement_func = refinement_func)

'''
print "Mesh Points:"
for i, p in enumerate(mesh.points):
    print i, p
print "Point numbers in tetrahedra:"
for i, t in enumerate(mesh.elements):
    print i, t
'''
#mesh.write_vtk("test.vtk")


#mymesh = refine(mesh, refinement_func = refinement_func)
mesh_points = np.array(mesh.points)
mesh_tris = np.array(mesh.elements)

import matplotlib.pyplot as plt
plt.triplot(mesh_points[:, 0], mesh_points[:, 1], mesh_tris)
plt.show()
