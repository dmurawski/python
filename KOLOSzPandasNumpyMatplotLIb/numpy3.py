import numpy as np 

def foo(n):
    n = int(n)
    tablica = np.arange(1,n*n+1)
    tablica = tablica.reshape((n,n))
    return print(tablica)

foo(5)