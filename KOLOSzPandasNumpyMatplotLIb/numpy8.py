import numpy as np
np.random.seed( 19680801 )
def foo(tablica,kierunek):
    print(tablica,"\n")
    if(kierunek=='pionowo'):
        if tablica.shape[1] %2==0:
            wymiar = tablica.shape[1]/2
            wymiar = int(wymiar)
            print(tablica[:,0:wymiar])
            print("\n",tablica[:,wymiar:])
        else:
            print("Nie da sie podzielic ze wzgeldu na ilosc kolumn")
    if(kierunek=='poziomo'):
        if tablica.shape[0] %2==0:
            wymiar = tablica.shape[0]/2
            wymiar = int(wymiar)
            print(tablica[0:wymiar])
            print("\n",tablica[wymiar:])
        else:
            print("Nie da sie podzielic ze wzgledu na ilosc wierszy")



tablica = np.random.rand(30)
tablica = tablica * 10
tablica = tablica.astype("int64")
tablica = tablica.reshape((6,5))
foo(tablica,'poziomo')

