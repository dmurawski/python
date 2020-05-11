import numpy as np
b = np.arange(12).reshape(3,4)
print(b)
b1 = np.arange(12).reshape(4,3)
print(b1)
b2 = np.arange(12).reshape(2,6)
print(b2)
for a in b.flat:
   # iterujemy jakby to była macierz płaska
   print(a)
print("====================")
for a in b1.flat:
   # iterujemy jakby to była macierz płaska
   print(a)
print("====================")
for a in b2.flat:
   # iterujemy jakby to była macierz płaska
   print(a)