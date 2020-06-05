import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.add_subplot( 3 , 2 , 1 , projection = '3d' )
ax2 = fig.add_subplot( 3 , 2 , 2 , projection = '3d' )
ax3 = fig.add_subplot( 3 , 2 , 3 , projection = '3d' )
ax4 = fig.add_subplot( 3 , 2 , 4 , projection = '3d' )
ax5 = fig.add_subplot( 3 , 2 , 5 , projection = '3d' )
ax6 = fig.add_subplot( 3 , 2 , 6 , projection = '3d' )

# generuj dane.
X = np.arange(- 5 , 5 , 0.25 )
Y = np.arange(- 5 , 5 , 0.25 )
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X** 2 + Y** 2 )
Z = np.sin(R)
# rysuj powierzchnię.
surf = ax.plot_surface(X, Y, Z, cmap =cm.spring,
linewidth = 0 , antialiased = False )
surf = ax2.plot_surface(X, Y, Z, cmap =cm.Wistia,
linewidth = 0 , antialiased = False )
surf = ax3.plot_surface(X, Y, Z, cmap =cm.hot,
linewidth = 0 , antialiased = False )
surf = ax4.plot_surface(X, Y, Z, cmap =cm.cool,
linewidth = 0 , antialiased = False )
surf = ax5.plot_surface(X, Y, Z, cmap =cm.summer,
linewidth = 0 , antialiased = False )
surf = ax6.plot_surface(X, Y, Z, cmap =cm.PiYG,
linewidth = 0 , antialiased = False )
ax.set_zlim(- 1.01 , 1.01 )
ax.zaxis.set_major_locator(LinearLocator( 10 ))
ax.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))
# Dodanie paska kolorów.
fig.colorbar(surf, shrink = 0.5 , aspect = 5 )
plt.show()
