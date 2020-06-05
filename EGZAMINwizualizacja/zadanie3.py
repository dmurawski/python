import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

dane = pd.read_csv("wyksz.csv")
wyzsze = dane[dane["wyksztalcenie"]=="wyzsze"]
#wazne sa wielkosc znakow
sred = dane[dane["wyksztalcenie"]=="srednie"]
podst = dane[dane["wyksztalcenie"]=="podstawowe"]
x=np.arange(0,len(wyzsze))#generowanie osi x 
#mozna tez tak x = [0,1,2] 
plt.bar(x,sred["Liczebnosc"],width=0.25,label="srednie",color="green")#wykres slupkowy,szerokosc slupka
plt.bar(x-0.25,wyzsze["Liczebnosc"],width=0.25,label="wyzsze",color="blue")#przesuniecie w lewo wykres slupkowy,szerokosc slupka
plt.bar(x+0.25,podst["Liczebnosc"],width=0.25,label="podstawowe",color="brown")# przesuniecie w prawo wykres slupkowy,szerokosc slupka
plt.legend(loc=7)#legenda,loc miejsce legendy
plt.title("TYTUŁ")
plt.xlabel("Przedział wiekowy")#etykieta osi x
plt.ylabel("Liczebnosc")#etykieta osi y
plt.xticks(x,podst["wiek"])#zmaina podpisu punktow na osi X
plt.show()