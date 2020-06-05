import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 30, 0.1)
s = np.sin(x)
c = np.sin(x)
plt.plot(x, s+2, label='sin(x)')
plt.plot(x-5,s,label='sin(x)')
plt.xlabel('arguemnty')
plt.ylabel('wartosci')
plt.title("Wykres sin(x),sin(x)")
plt.legend()
plt.show()