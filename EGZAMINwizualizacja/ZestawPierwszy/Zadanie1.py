#importujemy biblioteki
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 


x = np.arange(-5,10,step=0.01)#Przedzial w osi OX (od,do,skok)
y = (4-x+x**3)/(6+x-4*x**2+x**3) # Wartosci ze wzoru z zadania
plt.plot(x,y, color="lightblue",label="funkcja")#wykres liniowy (x,y,color,nazwa)
plt.ylim(-30,30)#przedzial w osi OY (od,do)
# asympotota pozioma
av=np.ones(len(x))#Generowanie asympototy poziomej za pomoca ones oraz dlugosc z len()
plt.plot(x,av,color="orange",linestyle='--',label="y=1")# wykres linowy (x,y,color,jak ma wygladac, nazwa)
# asymptota pionowa
x1=[-1,-1] #trzeba znalezc na wykresie
y1=[-30,30] #jak duza w OY
plt.plot(x1,y1, color="red",linestyle='--',label="x-1")#Generowanie asymptoty pionowej (x,y,color,jak ma wygladac, nazwa)
x2=[2,2] # trzeba znalezc na wykresie
y2=[-30,30] #jak duza w OY
plt.plot(x2,y2,color="green",linestyle="--",label='x=2')#Generowanie asymptoty pionowej (x,y,color,jak ma wygladac, nazwa)
x3=[3,3]# trzeba znalezc na wykresie
y3=[-30,30]#jak duza w OY
plt.plot(x3,y3,color='violet',linestyle="--",label='x=3')#Generowanie asymptoty pionowej (x,y,color,jak ma wygladac, nazwa)
plt.title("Wykres funkcji") # Tytul wykresu
plt.legend() #dodawanie legendy trzeba dodwac label(nazwe/etykiete) do wykresow
#aby zmienic lokalizacje legendy trzeba uzyc plt.legend(loc=ODPOWIEDNIA CYFRA)
plt.savefig("zad1.pdf",format='pdf')#Zapis musi byc przed plt.show() oraz zawierac format
plt.show() # pokazywanie wykresow