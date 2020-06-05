import numpy as np 

macierz1 = np.random.randint(100,size=(6))
macierz1 = macierz1.reshape(2,3)
print(macierz1)
a = np.sin(macierz1)
print(a)