import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import re
holder = []
with open("Au6.wrl", "rb") as vrml:
    for lines in vrml:
    	print lines
        a = re.findall("[-0-9]{1,3}.[0-9]{6}", lines)
        if len(a) == 3:
            holder.append(map(float, a))

holder_array = np.array(holder) #if you want numpy array

#3D Plotting
x,y,z = zip(*holder)
fig = plt.figure()
ax = Axes3D(fig)
ax.plot(x,y,z)
plt.show()