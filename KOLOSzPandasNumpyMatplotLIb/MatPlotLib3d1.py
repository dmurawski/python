import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import numpy as np 


z = np.linspace(0,2*np.pi)
x = np.sin(z)
y = 2*(np.cos(z))

plt.plot(x,y,color="orange")
plt.show()