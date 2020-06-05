import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 


dane = pd.read_csv("Nowy folder (2)/movie.csv")
#print(dane)
# naj=dane.dtypes.value_counts().head(1)
# naj=naj.index.values
# # print(naj)
# def get_statistical_params(x,naj):
#     x=x.select_dtypes(include=naj)
#     print(x.describe().T)
# get_statistical_params(dane,naj)

# def add_actor_total_fb_likes(x):
#     x['add_actor_total_fb_likes']=x['actor_1_facebook_likes'] + x['actor_2_facebook_likes'] + x['actor_3_facebook_likes']
#     print(x)

# add_actor_total_fb_likes(dane)

# def get_min_imdb_score(x):
#     x = x.sort_values(by='imdb_score').head(10)
#     x = x[['movie_title','imdb_score']]
#     x = np.array(x)
#     print(type(x))
#     print(x)

# get_min_imdb_score(dane)


# def get_rows_cols(dane,X,Y,Z):
#     x = dane.iloc[X:Y,::] #  wiersze od ilu do ilu
#     x = x.iloc[::(X+Z)] # wiersze co ile
#     x = x.iloc[:,::Z] # Po kolumnach ile ma ich byc
#     print(x)



# X = 3 
# Y = 21 * 5
# Z = 4
# get_rows_cols(dane,X,Y,Z)

X = 3 
Y = 21 * 5
Z = 4

plt.subplot(3,3,1)
x = dane.head(8)
nazwy = x["movie_title"]
wartosci = x["duration"]
plt.bar(nazwy,wartosci,label="dlugosc filmu")
plt.xticks(rotation=90)
plt.legend(title="legenda",bbox_to_anchor=(1.3, 1.05))
plt.title("Dlugosc filmow")
plt.ylabel("czas w min")

plt.subplot(3,3,5)
wartosci1 = x['actor_1_facebook_likes']
losowaWartoscX = np.random.randint(X,Y,1)
kolor = np.random.randint(X,3*X,8)
rozmiar = np.random.randint(X,X+Z,8)
wartosci1 = wartosci1*losowaWartoscX
wartosci2 = x['actor_3_facebook_likes']
wartosci2 = wartosci2*losowaWartoscX
plt.scatter(wartosci1,wartosci2,c=kolor,s=rozmiar)
plt.title("Wykres punktowy")

plt.subplot(3,3,9)
kolowy = x[['director_name','movie_title']]
kolowy = kolowy.groupby(by='director_name').count()
print(kolowy)
plt.pie(kolowy,labels = kolowy.index.values,autopct="%1.1f%%")
plt.legend(bbox_to_anchor=(2.3, 1.05))
plt.title("Udzial rezysera")
plt.show()