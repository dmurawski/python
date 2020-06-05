import numpy as np 


macierz1 = np.arange(1,10,1)*12-6
macierz1 = macierz1.reshape(3,3)
print(macierz1,'\n')
print(macierz1.min(axis=0))
print(macierz1.min(axis=1))
print('\n')
macierz2 = np.arange(2,18,1)*12-6
macierz2 = macierz2.reshape(4,4)
print(macierz2,'\n')
print(macierz2.min(axis=0))
print(macierz2.min(axis=1))
