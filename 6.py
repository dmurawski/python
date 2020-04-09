import math

def promien(a, b, x, y):
    r = math.sqrt(((x - a) ** 2) + ((y - b) ** 2))
    return r
print("Promien",promien(2,1,6,4))