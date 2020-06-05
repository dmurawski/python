import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

dane = pd.read_excel("sport.xlsx",header=None)
#ścieżka dostepi do pliku(nazwa pliku np:"sport.xlsx") header to nagłówek
x = dane.iloc[:,1]#indeksowanie procenty
etykiety = dane.iloc[:,0]#podpisy
plt.pie(x,labels=etykiety,autopct="%1.1f%%",explode=(0.1,0,0,0,0,0))#wykres kolowy od x,etykiety,wypisane procenty explode odsuniecie od srodka
plt.title("TYTUŁ WYKRESU")
plt.annotate("12345",[-1,1])#dodanie tekstu w lewym gornym rogu
#plt.text tym tez mozna dodac tekst do wykresu
plt.savefig("zad2.jpg")#zapisanie do jpg
plt.show()