import math
def suma(a1 = 1, r = 1, n = 10):
    suma = ((2 * a1 + (n - 1) * r) / 2) * n
    return suma
print("Wynik: ",suma(1,10,4))