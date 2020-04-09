def suma(a1 , r , n ):
    suma = ((2 * a1 + (n - 1) * r) / 2) * n
    print("Wynik sumowania: ",suma)

def iloczyn(a1, n, r):
    i = 0
    an = 1
    suma = 1
    while i < n:
        suma = suma * an
        an = a1 + (n - i - 1) * r
        print(an)
        i += 1
    print("wynik iloczyn",suma)

def n_element(a1, n ,r):
    an = a1 + (n - 1) * r
    print("wynik n_element:",an)