import numpy as np 


macierzORIGIN = np.random.randint(600,size=12,dtype='int64')
print(macierzORIGIN)
macierz = macierzORIGIN.reshape(3,4)
macierz2 = macierzORIGIN.reshape(4,3)
macierz3 = macierzORIGIN.reshape(2,6)
for a in macierz.flat:
    print(a,end=" ")
print('\n')
for a in macierz2.flat:
    print(a,end=" ")
print('\n')
for a in macierz3.flat:
    print(a,end=" ")
