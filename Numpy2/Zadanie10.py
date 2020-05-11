import numpy as np
# generujemy macierz 3x2
b = np.arange(81).reshape(9,9)
print(b)
b = b.reshape(81,1)
print(b)
b = b.reshape(1,81)
print(b)
# chyba istnieja tylko 2 sposoby poniewaz nie mozna inaczej tej macierzy przekształcic