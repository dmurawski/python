import pandas as pd 
import numpy as np 

dane = pd.read_excel("D:/Damian/python/KOLOSzPandasNumpyMatplotLIb/imiona.xlsx")
# print(dane)
print(dane[dane['Liczba']>1000])
print(dane[dane['Imie']=='DAMIAN'])
suma=dane['Liczba'].sum(axis=0)
print("Ilosć urodzeń: ",suma)
suma2=dane[(dane['Rok']>1999) & (dane['Rok']<2006)]
suma2=suma2['Liczba'].sum(axis=0)
print("Ilosć urodzeń 2000-2005: ",suma2)
print("\n")
print(dane.groupby(['Plec']).agg({'Liczba':['sum']}))
print("\n")
#print(dane.sort_values(by=['Rok','Liczba'],ascending=False))
#print(dane['Liczba'].nlargest(2))
#dane34 = dane.groupby(['Imie']).agg({'Liczba':['sum']})
#dane35 = dane34.sort_values(by=('Liczba','sum'),ascending=False)
#print(dane35.head(2))
x = dane.sort_values('Liczba', ascending=False).groupby(['Plec']).head(1)
print(x)

#x = dane.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).head(1)
#print(x)



