import numpy as np 

macierz = np.random.randint(100,size=9,dtype='int64')
macierz = macierz.reshape(3,3)
print(macierz)
for a in macierz.flat:
    print(a,end=" ")