import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

x = np.arange(0,30,0.1)
y = np.sin(x)
plt.plot(x,y+2,color='blue',label="sin(x)")
plt.plot(x,-y,color='orange',label ="sin(x)")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("Wykres sin(x), sin(x)")
plt.legend(loc=6)
plt.show()