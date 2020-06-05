import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0, 40, 0.5)


sin = np.sin(x)
cos = np.cos(x)
plt.plot(x, sin, label='sin(x)')

plt.plot(x,cos,label='cos(x)')


plt.ylabel('Y')
plt.xlabel('X')
plt.title("SINUS I COSINUS")
plt.legend()


plt.show()