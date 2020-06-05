import numpy as np 

def foo(n):
    i = 0
    z = 1
    ii = 1
    zz = 2
    a = np.zeros((n,n))
    while i < n: 
        a = a + np.diag(np.full(n-i,2*z),i)
        a = a + np.diag(np.full(n-ii,2*zz),-ii)
        i = i + 1
        z = z + 1
        ii = ii + 1
        zz = zz + 1
    print(a)

foo(5)