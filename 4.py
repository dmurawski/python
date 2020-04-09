import math
def monotonicznosc(a, x, b):
    y = a * x + b
    if(a < 0):
        print("malejaca")
    elif(a == 0):
        print("stala")
    else:
        print("rosnaca")
    return y
print(monotonicznosc(1,2,3))