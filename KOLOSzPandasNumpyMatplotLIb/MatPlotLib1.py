import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(0,20) # start stop ile pkt
plt.plot(x,1/x, label="wykers 1")
plt.ylabel("F(x)")
plt.xlabel("x")
plt.xlim([1,20])
plt.ylim([0,1])
plt.legend()
plt.show()