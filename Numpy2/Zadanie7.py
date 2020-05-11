import numpy as np

def dodawanieMacierzy(a, b):
    c = 0
    c = a + b
    print(c)


a = np.arange(6)
a = a.reshape(2, 3)
print(a)
b = np.arange(6, 12)
b = b.reshape(2, 3)
print(b)
dodawanieMacierzy(a,b)
