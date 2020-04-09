matrix = [
    [ 1, 2, 3, 3 ],
    [ 2, 3, 2, 3 ],
    [ 4, 1, 2, 1 ],
    [ 9, 0, 7, 2 ],
]
print("matrix:")
for row in matrix:
    print(row)

print("\nPrzekatna\n")

przekatna = [x[y] for y,x in enumerate(matrix)]
print(przekatna)