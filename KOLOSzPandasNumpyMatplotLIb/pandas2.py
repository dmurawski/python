import numpy as np 
import pandas as pd 

url = "https://raw.githubusercontent.com/kropiak/wd/master/8_pandas_1/datasets/zamowienia.csv"
dane = pd.read_csv(url, error_bad_lines=False,delimiter=";")
# print(dane)

# 1   x = dane['Sprzedawca'].unique()
# print(x)

# 2    x = dane.sort_values(by=('Utarg'),ascending=False).head(5)
# print(x)

# 3 x = dane.groupby(['Sprzedawca']).count()
# print(x['idZamowienia'])

# 4 x = dane.groupby(['Kraj']).count()
# print(x['idZamowienia'])

# 5 x=dane[(dane['Kraj']=='Polska') & (dane['Data zamowienia']>='2005-01-01')& (dane['Data zamowienia']<'2006-01-01')].count()
#print(x['Kraj'])


# 6  x=dane[(dane['Data zamowienia']>='2004-01-01')& (dane['Data zamowienia']<'2005-01-01')].mean()
# print(x['idZamowienia'])

# rok2005=dane[(dane['Kraj']=='Polska') & (dane['Data zamowienia']>='2005-01-01')& (dane['Data zamowienia']<'2006-01-01')]
# print(rok2005)
# rok2005.to_csv('D:/Damian/python/KOLOSzPandasNumpyMatplotLIb/zamowienia_2005.csv')


#rok2004=dane[(dane['Kraj']=='Polska') & (dane['Data zamowienia']>='2004-01-01')& (dane['Data zamowienia']<'2005-01-01')]
#print(rok2004)
#rok2004.to_csv('D:/Damian/python/KOLOSzPandasNumpyMatplotLIb/zamowienia_2004.csv')