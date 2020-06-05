import numpy as np 

macierz = np.random.randint(100,size=81,dtype='int64')
macierz = macierz.reshape(9,9)
print(macierz)

macierz = macierz.reshape(27,3)
print(macierz)
print('\n')
macierz = macierz.reshape(3,27)
print(macierz)
print('\n')
macierz = macierz.reshape(1,81)
print(macierz)
print('\n')
macierz = macierz.reshape(81,1)
print(macierz)
print('\n')