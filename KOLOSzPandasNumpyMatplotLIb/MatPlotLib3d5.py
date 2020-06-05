import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.add_subplot( 1 , 2 , 1 , projection = '3d' )
ax2 = fig.add_subplot( 1 , 2 , 2 , projection = '3d' )
X = np.arange(- 5 , 5 , 0.25 )
Y = np.arange(- 5 , 5 , 0.25 )
XX = np.arange(- 5 , 5 , 0.1 )
YY = np.arange(- 5 , 5 , 0.1 )
X, Y = np.meshgrid(X, Y)
XX, YY = np.meshgrid(XX,YY)
RR = np.sqrt(XX** 2 + YY** 2 )
R = np.sqrt(X** 2 + Y** 2 )
Z = np.sin(R)
ZZ = np.sin(RR)
surf = ax.plot_surface(X, Y, Z, cmap =cm.coolwarm,
linewidth = 0 , antialiased = False )
#fig.colorbar(surf, shrink = 1 , aspect = 5 )
surf2 = ax2.plot_surface(XX, YY, ZZ, cmap =cm.summer,
linewidth = 0 , antialiased = True )
#fig.colorbar(surf2, shrink = 1 , aspect = 5 )
ax2.set_zlim(- 1.01 , 1.01 )
ax2.zaxis.set_major_locator(LinearLocator( 10 ))
ax2.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))
ax.set_zlim(- 1.01 , 1.01 )
ax.zaxis.set_major_locator(LinearLocator( 10 ))
ax.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))
plt.show()
