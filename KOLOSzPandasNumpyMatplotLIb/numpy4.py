import numpy as np 

def foo(n,podstawa):
    tablica = np.logspace(1, n,num=n, base=podstawa, dtype='int64')
    return print(tablica)

foo(5,2)