import numpy as np
def funkcja(n):
    i = 0
    z = 1
    a = np.zeros((n,n))
    while i < n: 
        a = a + np.diag(np.full(n-i,2*z),i)
        i = i + 1
        z = z + 1
    i = 1
    z = 2
    while i < n: 
        a = a + np.diag(np.full(n-i,2*z),-i)
        i = i + 1
        z = z + 1
    print(a)
funkcja(3)




