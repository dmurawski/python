import numpy as np
import matplotlib.pyplot as plt


x = np.arange(1,21,1)
plt.plot(x, 1/x)
plt.ylabel('Os y')
plt.xlabel('Os X')
plt.axis([0, 20, 0, 1])
plt.show()