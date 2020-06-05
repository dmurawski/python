import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from mpl_toolkits.mplot3d.axes3d import get_test_data
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure( figsize =plt.figaspect( 0.2 ))
ax1 = fig.add_subplot( 1 , 2 , 1 )
X = np.arange(0 , 20 , 1 )
Y = np.arange(0, 20 , 1 )
X1 = np.arange(0 ,5 , 1 )
Y2 = np.arange(-2, 3 , 1 )

ax1= plt.plot(X, Y**2, 'g^')
ax1=plt.xlabel('etykieta x')
ax1=plt.ylabel('etykieta y')
ax1=plt.title("Prosty wykres")
ax2 = fig.add_subplot( 1 , 2 , 2 )
ax2=plt.plot (X1, abs(Y2*2), label= 'liniowy')
ax2=plt.plot (X1, abs(Y2*2), 'r+')
ax2=plt.xlabel('etykieta x')
ax2=plt.ylabel('etykieta y')
ax2=plt.title("Prosty wykres")
plt.show()
