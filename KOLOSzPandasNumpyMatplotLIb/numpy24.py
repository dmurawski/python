import numpy as np 

macierz1 = np.arange(1,4,1,dtype="int64")
macierz1 = macierz1.reshape(1,3)
print(macierz1)
macierz2 = np.arange(1,4,1,dtype="float")/2*23
macierz2 = macierz2.reshape(1,3)
print(macierz2)
macierzSuma = macierz1 * macierz2
print(macierzSuma)