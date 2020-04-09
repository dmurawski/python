import math
def ciag(a1, n, r):
    i = 0
    an = 1
    suma = 1
    while i < n:
        suma = suma * an
        an = a1 + (n - i - 1) * r
        print(an)
        i += 1
    return suma
print("wynik: ",ciag(1,5,2))
    
    