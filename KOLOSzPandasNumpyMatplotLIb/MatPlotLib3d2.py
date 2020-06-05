import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import numpy as np 

x = np.arange(1,10,1)
y = np.random.randint(1,10,size=9)
y2 = np.random.randint(1,10,size=9)
y4 = np.random.randint(1,10,size=9)
y5 = np.random.randint(1,10,size=9)
y6 = np.random.randint(1,10,size=9)
plt.plot(x,y, '.g')
plt.plot(x,y2, '.g')
plt.plot(x,y4, '.y')
plt.plot(x,y5, '.',color="brown")
plt.plot(x,y, '.r')
plt.show()