import math
def rowno_czy_prosto(a, b, x, a2, b2):
    y = a * x + b
    y2 = a2 * x + b2
    if(a == a2):
        print("rownolegle")
    elif(a * a2 == -1):
        print("prostopadle")
    else:
        print("nie monotoniczna")
    return y,y2
print(rowno_czy_prosto(3,2,3,(-1/3)*(-9),4))
