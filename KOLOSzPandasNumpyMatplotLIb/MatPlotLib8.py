import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

def rzucaj(n,list):
    for n in range(n):
        a=np.random.randint(1,7)
        b=np.random.randint(1,7)
        c=a+b
        list.append(c)


list =[]
rzucaj(500,list)
plt.hist(list, density=True)
plt.grid(True)
plt.xlabel('Wartości')
plt.ylabel('Szansa')
plt.title('Histogram')
plt.show()