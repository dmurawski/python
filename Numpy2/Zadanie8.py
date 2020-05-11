import numpy as np


a = np.arange(9,18)
a = a.reshape(3, 3)
print(a)
y = 0
x = 0
while y < 3:
        print(a[x][y])
        y = y + 1
y=0
x=1
print("===================")
while y < 3:
        print(a[x][y])
        y = y + 1
y=0
x=2
print("===================")
while y < 3:
        print(a[x][y])
        y = y + 1