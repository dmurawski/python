import numpy as np 

def foo(dlugosc):
    wektor = np.arange(dlugosc,0,-1)
    wektorDiag = np.diag(wektor)
    return print(wektor,"\n",wektorDiag)

foo(3)