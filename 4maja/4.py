import numpy as np
def funkcja(liczba,n):
    x = np.logspace(1,n,num=n,base=liczba,dtype='int')
    print(x)
funkcja(2,4)
