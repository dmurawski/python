import numpy as np 

fibo=[1,1]
for x in range(23):
    fibo.append(fibo[-2]+fibo[-1])
print(fibo)
fibo = np.array(fibo)
fibo = fibo.reshape((5,5))
print("\n",fibo)
    

