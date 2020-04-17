plik = open("kolejna_praca/plikdo1.py","w+")
import random
from random import randint 
list = []
list = [random.randrange(0, 1000, 4)]
print(list)
plik.write(str(list))
plik.close()