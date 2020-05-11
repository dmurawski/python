import numpy as np

a = np.arange(9)
a = a.reshape(3, 3)
print(a)
b = np.arange(16)
b = b.reshape(4, 4)
print(b)
print(b.min(axis=0))
print(b.min(axis=1))
print(a.min(axis=0))
print(a.min(axis=1))