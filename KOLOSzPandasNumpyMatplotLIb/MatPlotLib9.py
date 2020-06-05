import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

url = "https://raw.githubusercontent.com/kropiak/wd/master/8_pandas_1/datasets/zamowienia.csv"
dane = pd.read_csv(url, error_bad_lines=False,delimiter=";")
y = dane['Sprzedawca'].unique()
print(y)
x=dane.groupby('Sprzedawca').sum()
x=x['Utarg']
print(x)
plt.pie(x,autopct="%1.1f%%",labels=x.index.values,shadow=True,explode=(0,0,0,0,0,0,0,0.1,0))
plt.title("Wykres Utargu")
plt.savefig("zad2.png")#zapisanie do jpg
plt.show()



# dane = pd.read_excel("sport.xlsx",header=None)
# #ścieżka dostepi do pliku(nazwa pliku np:"sport.xlsx") header to nagłówek
# x = dane.iloc[:,1]#indeksowanie procenty
# etykiety = dane.iloc[:,0]#podpisy
# plt.pie(x,labels=etykiety,autopct="%1.1f%%",explode=(0.1,0,0,0,0,0))#wykres kolowy od x,etykiety,wypisane procenty explode odsuniecie od srodka
# plt.title("TYTUŁ WYKRESU")
# plt.annotate("12345",[-1,1])#dodanie tekstu w lewym gornym rogu
# #plt.text tym tez mozna dodac tekst do wykresu
# plt.savefig("zad2.jpg")#zapisanie do jpg
# plt.show()