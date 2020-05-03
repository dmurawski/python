import numpy as np
def funkcja(n):
    a = np.arange(n, 0,-1)
    print(a)
    b = np.diag(a)
    print("\n")
    print(b)

funkcja(3)