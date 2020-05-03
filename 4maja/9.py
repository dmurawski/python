import numpy as np
fib = np.array([1,1])
for i in range(0,23):
    fib = np.append(fib, fib[-2] + fib[-1])
    x = np.array(fib)
x = x.reshape(5,5)
print(x)