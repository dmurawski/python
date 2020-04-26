def fibb(n):
    a, b = 0, 1
    for n in range(n):
        a, b = b, a + b
        yield (a)

fibbonaci = fibb(21)
print(next(fibbonaci))
print(next(fibbonaci))
print(next(fibbonaci))
print(next(fibbonaci))
print(next(fibbonaci))
print(next(fibbonaci))
print(next(fibbonaci))
print(next(fibbonaci))
print(next(fibbonaci))
print(next(fibbonaci))
print(next(fibbonaci))
print(next(fibbonaci))