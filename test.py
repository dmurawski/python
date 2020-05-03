import numpy as np
def funkcja(n):
    i = 1
    while i<=n:
        a = np.arange(i*i)
        a = a.reshape(i, i)
        print("==========")
        print(a)
        i = i + 1

funkcja(6)
    
    