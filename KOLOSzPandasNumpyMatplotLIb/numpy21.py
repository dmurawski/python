import numpy as np 

macierz1 = np.arange(1,4,1)
macierz1 = macierz1.reshape(3,1)
print(macierz1)
macierz2 = np.arange(1,4,1)*3-5
macierz2 = macierz2.reshape(3,1)
print('\n',macierz2)
macierzSuma = macierz1 * macierz2
print('\n',macierzSuma)