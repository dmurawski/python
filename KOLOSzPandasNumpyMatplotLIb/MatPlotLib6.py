import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

dane = pd.read_excel("D:/Damian/python/KOLOSzPandasNumpyMatplotLIb/imiona.xlsx")

plt.subplot(3,1,1)
Plec = ['Dziewczyny','Chlopaki']
Chlopaki = dane.groupby("Plec")
Urodzenia = Chlopaki['Liczba'].sum()
plt.bar(Plec,Urodzenia,width=0.25,label="Ilosc Urodzen",color="blue")
plt.xlabel('Plec')
plt.ylabel('Ilosc narodzin')
plt.xticks(Plec)
plt.title("Urodzenia")
plt.legend()

plt.subplot(3,1,2)
K=(dane.groupby(['Plec','Rok']).agg(sum).loc['K'])['Liczba']
M=(dane.groupby(['Plec','Rok']).agg(sum).loc['M'])['Liczba']
plt.xlabel('x')
plt.ylabel('y')
plt.plot(K.index.values,K.values, label='Kobiety')
plt.plot(M.index.values,M.values, label='Mężczyżni')
plt.legend()

plt.subplot(3,1,3)
x6 = dane['Rok']
y6 = dane['Liczba']
plt.bar(x6,y6,label="Wykres")
plt.legend()
plt.show()