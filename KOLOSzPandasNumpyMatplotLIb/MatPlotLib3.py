import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

x = np.arange(0,30,0.1)
y = np.sin(x)
plt.plot(x,y,label="f(x)=sin(x)")
plt.xlabel("Oś OX")
plt.ylabel("Oś OY")
plt.title("Wykres funkcji sin(x)")
plt.legend()
plt.show()