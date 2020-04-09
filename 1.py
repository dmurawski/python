A = [1/x for x in range(1,11,1)]
print(A)
B = [2**x for x in range(0,11,1)]
print(B)
C = [x for x in B if x % 4 == 0]
print(C)