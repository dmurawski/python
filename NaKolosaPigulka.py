#Jak wczytywać pliki z komputera do pliku .py

# x = pd.read_csv("Sciezka pliku",delimiter="Jesli potrzebny",header="Ktory to naglowego",skiprows="ile ma ominac lini") ---------- Czytanie csv
# x = pd.read_excel("Sciezka pliku",delimiter="Jesli potrzebny",header="Ktory to naglowego",skiprows="ile ma ominac lini") ---------- Czytanie EXCEL

#Jak zapisywac pliki 

#plt.savefig("zad1.pdf",format='pdf')#Zapis musi byc przed plt.show() oraz zawierac format

# JAK RYSOWAC WYKRES PUNKTOWY
# plt.scatter(x,y,color,marker,size)
# plt.subplot(x,y,z) ile na ile oraz ktore miejsce zajmuje
# plt.legend(bbox_to_anchor=(2.3, 1.05) albo loc=, title="legenda") Przesuwanie legendy
# plt.xticks(rotation=90) obort nazw z osi OX

# PODZIAL TABELI NA CZESCI

# y=x.iloc[X:Y,::] Podzial wierszami od X do Y
# y=y.iloc[::(X+Z)] Podzial CO X+Y np co 6 lini
# kolumny=x.iloc[:,::Z] Podzial kolumnami co Z

#naj=x.dtypes.value_counts().head(1) 
# naj=naj.index.values
#Najcześciej wystepujacy typ w danej tabeli np Float64


#WYKRES SLUPKOWY

# wyzsze = dane[dane["wyksztalcenie"]=="wyzsze"]
#wazne sa wielkosc znakow
#sred = dane[dane["wyksztalcenie"]=="srednie"]
#podst = dane[dane["wyksztalcenie"]=="podstawowe"]
#x=np.arange(0,len(wyzsze))#generowanie osi x 
#mozna tez tak x = [0,1,2] 
#plt.bar(x,sred["Liczebnosc"],width=0.25,label="srednie",color="green")#wykres slupkowy,szerokosc slupka
#plt.bar(x-0.25,wyzsze["Liczebnosc"],width=0.25,label="wyzsze",color="blue")#przesuniecie w lewo wykres slupkowy,szerokosc slupka
#plt.bar(x+0.25,podst["Liczebnosc"],width=0.25,label="podstawowe",color="brown")# przesuniecie w prawo wykres slupkowy,szerokosc slupka
#plt.legend(loc=7)#legenda,loc miejsce legendy
#plt.title("TYTUŁ")
#plt.xlabel("Przedział wiekowy")#etykieta osi x
#plt.ylabel("Liczebnosc")#etykieta osi y
#plt.xticks(x,podst["wiek"])#zmaina podpisu punktow na osi X
#plt.show()


#Wykres KOLOWY

#ścieżka dostepi do pliku(nazwa pliku np:"sport.xlsx") header to nagłówek
#x = dane.iloc[:,1]#indeksowanie procenty
#etykiety = dane.iloc[:,0]#podpisy
#plt.pie(x,labels=etykiety,autopct="%1.1f%%",explode=(0.1,0,0,0,0,0))#wykres kolowy od x,etykiety,wypisane procenty explode odsuniecie od srodka
#plt.title("TYTUŁ WYKRESU")
#plt.annotate("12345",[-1,1])#dodanie tekstu w lewym gornym rogu
#plt.text tym tez mozna dodac tekst do wykresu
#plt.savefig("zad2.jpg")#zapisanie do jpg
#plt.show()


# Wykres podwojny

#x = pd.ExcelFile('D:/Damian/python/KOLOSzPandasNumpyMatplotLIb/imiona.xlsx')
#imiona = pd.read_excel(x,'Arkusz1')
#imiona.yaxis.set_major_locator(MaxNLocator(integer=True))
#K=(imiona.groupby(['Plec','Rok']).agg(sum).loc['K'])['Liczba']
#M=(imiona.groupby(['Plec','Rok']).agg(sum).loc['M'])['Liczba']

#plt.bar(K.index.values,K.values, label='Kobiety')
#plt.bar(M.index.values,M.values, label='Mezczyzni', bottom = K.values)
#plt.legend()



# PANDAS AGREGACJA I SORTOWANIE 


# def zadanie1(dane):
#     print(dane[dane['Liczba']>1000])

# def zadanie2(dane):
#     print(dane[dane['Imie']=="SEBASTIAN"])

# def zadanie3(dane):
#     liczbaUrodzen = dane['Liczba'].sum()
#     print("Liczba urodzen: ", liczbaUrodzen)

# def zadanie4(dane):
#     przedzialLat = dane[(dane['Rok']>=2000) & (dane['Rok'] <=2005)]
#     ilosc = przedzialLat['Liczba'].sum()
#     print("Ilosc dzieci urodzony miedzy 2000-2005: ",ilosc)

# def zadanie5(dane):
#     M = dane.Liczba[dane.Plec == 'M']
#     K = dane.Liczba[dane.Plec == 'K']
#     print("Suma chlopcow: ",sum(M),"suma dziewczat:",sum(K))

# def zadanie6(dane):
#     print(dane.sort_values('Liczba',ascending=False).groupby(['Rok','Plec']).nth(0))
    
# def zadanie7(dane):
#     print(dane.sort_values('Liczba',ascending=False).groupby(['Plec']).head(1))


# def zadanie1(dane):
#     print(dane['Sprzedawca'].unique())

# def zadanie2(dane):
#     print(dane.sort_values(['Utarg'],ascending=False).head(5))

# def zadanie3(dane):
#     print(dane.groupby('Sprzedawca').count())

# def zadanie4(dane):
#     x = dane.groupby('Kraj').count()
#     print(x['idZamowienia'])

# def zadanie5(dane):
#     liczba = dane[(dane['Kraj']=='Polska') & (dane['Data zamowienia'] >= '2005-01-01') & (dane['Data zamowienia'] <= '2006-01-01')].count()
#     print("Ilosc zamowien:",liczba['idZamowienia'])

# def zadanie6(dane):
#     srednia = dane[(dane['Data zamowienia']>='2004-01-01') & (dane['Data zamowienia']<='2005-01-01')]
#     srednia2 = srednia['Utarg'].mean()
#     print(srednia2)
# def zadanie7(dane):
#     rok2005=dane[(dane['Kraj']=='Polska') & (dane['Data zamowienia']>='2005-01-01')& (dane['Data zamowienia']<'2006-01-01')]
#     print(rok2005)
#     rok2005.to_csv('D:/Damian/python/KOLOSzPandasNumpyMatplotLIb/zamowieniaSM_2005.csv')

#     rok2004=dane[(dane['Kraj']=='Polska') & (dane['Data zamowienia']>='2005-01-01')& (dane['Data zamowienia']<'2006-01-01')]
#     print(rok2004)
#     rok2004.to_csv('D:/Damian/python/KOLOSzPandasNumpyMatplotLIb/zamowieniaSM_2004.csv')


