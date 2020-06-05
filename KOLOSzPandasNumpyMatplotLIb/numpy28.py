import numpy as np 

macierz = np.random.randint(100,size=9,dtype='int64')
macierz = macierz.reshape(3,3)
print(macierz)
y=0
x=0
while y<3:
    print(macierz[0][y])
    y=y+1
y=0
print('\n')
while y<3:
    print(macierz[1][y])
    y=y+1
y=0
print('\n')
while y<3:
    print(macierz[2][y])
    y=y+1
