import numpy as np

def funkcja(matrix,kierunek):
    print(matrix)
    if kierunek == 0:
        if matrix.shape[0] %2==0:
            stala = matrix.shape[0] / 2
            stala = int(stala)
            print('\n')
            print(matrix[0:stala])
            print('\n')
            print(matrix[stala:])
        if matrix.shape[0] %2==1:
            print("Nie mozna wiersze!")
    if kierunek == 1:
        if matrix.shape[1] %2==0:
            stala = matrix.shape[1] / 2
            stala = int(stala)
            print('\n')
            print(matrix[:,0:stala])
            print('\n')
            print(matrix[:,stala:])
        if matrix.shape[1] %2==1:
            print("Nie mozna kolumny!")

mat = np.arange(32)
mat = mat.reshape((4,8))
funkcja(mat, 0)
