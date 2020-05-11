import numpy as np

a = np.arange(3)
a = a.reshape(1, 3)
print(a)
b = np.arange(3,6)
b = b.reshape(1, 3)
print(b)

a = a*b
print(a)
    