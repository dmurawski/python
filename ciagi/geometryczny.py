def suma(a1 , n , q ):
    if(q == 1):
        suma = a1 * n
    else:
        suma = a1 * ((1 - q ** n)/(1-q))
    print("Wynik sumowania geo: ",suma)

def iloczyn(a1, n, q):
    i = 0
    an = 1
    suma = 1
    while i < n:
        suma = suma * an
        an = a1 * q ** (n - i - 1)
        print(an)
        i += 1
    print("wynik iloczyn geo:",suma)

def n_element(a1, n ,q):
    an = a1 * q ** (n-1)
    print("wynik n_element geo:",an)