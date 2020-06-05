import numpy as np 
import pandas as pd 
import xlrd
from matplotlib.ticker import MaxNLocator
import openpyxl
import matplotlib.pyplot as plt

x = pd.ExcelFile('D:/Damian/python/KOLOSzPandasNumpyMatplotLIb/imiona.xlsx')
imiona = pd.read_excel(x,'Arkusz1')
#imiona.yaxis.set_major_locator(MaxNLocator(integer=True))
K=(imiona.groupby(['Plec','Rok']).agg(sum).loc['K'])['Liczba']
M=(imiona.groupby(['Plec','Rok']).agg(sum).loc['M'])['Liczba']

plt.bar(K.index.values,K.values, label='Kobiety')
plt.bar(M.index.values,M.values, label='Mezczyzni', bottom = K.values)
plt.legend()


plt.show()