import numpy as np
def funkcja(n):
    a = np.arange(1,(n*n)+1,1)
    a = a.reshape(n, n)
    print(a)
funkcja(5)
    
    