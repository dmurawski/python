import numpy
b = numpy.arange(12).reshape(3,4)
print(b)
b1 = numpy.arange(12).reshape(4,3)
print(b1)
b2 = numpy.arange(12).reshape(2,6)
print(b2)
for a in b.flat:
   print(a)
print("\n")
for a in b1.flat:
   print(a)
print("\n")
for a in b2.flat:
   print(a)