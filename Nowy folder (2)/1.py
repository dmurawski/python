import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

x = pd.read_csv("Nowy folder (2)/movie.csv")
print(x.T)
naj=x.dtypes.value_counts().head(1)
naj=naj.index.values
# print(naj)
def get_statistical_params(x,naj):
    x=x.select_dtypes(include=naj)
    print(x.describe().T)
get_statistical_params(x,naj)

# def add_actor_total_fb_likes(x):
#     sum = x['actor_1_facebook_likes']+x['actor_2_facebook_likes']+x['actor_3_facebook_likes']
#     x['actor_total_fb_likes']=sum
#     print(x)
# add_actor_total_fb_likes(x)

# def get_min_imdb_score(x):
#     y=x.sort_values(by=['imdb_score']).head(10)
#     y=y['movie_title']
#     print(y)
#     print(type(y))
#     y=np.array(y)
#     print(y)
#     print(type(y))
# get_min_imdb_score(x)
# def get_min_imdb_score(x):
#     y=x.nsmallest(10,'imdb_score')
#     y=y['movie_title'].values
#     y=np.array(y)
#     print(y)
#     print(type(y))



# get_min_imdb_score(x)
# X=3
# Y=22*5
# Z=3
# a=X

# def get_rows_cols(x,X,Y,Z):
#     y=x.iloc[X:Y,::]
#     y=y.iloc[::(X+Z)]
#     print(y)
#     print(type(y))
#     kolumny=x.iloc[:,::Z]
#     print(kolumny)
#     print(type(kolumny))


# get_rows_cols(x,X,Y,Z)

# def wykres(x):

#     plt.subplot(3,3,1)
#     tytuly =  x['movie_title'].head(8)
#     plt.xticks(rotation=90)
#     dlugosc = x['duration'].head(8)
#     print(tytuly)
#     plt.bar(tytuly,dlugosc,label="Legenda")
#     plt.title("Dlugosc filmow")
#     plt.legend(title="legenda",bbox_to_anchor=(1, 1.05))

#     plt.subplot(3,3,5)
#     plt.title("wykres punktowy")
#     LosowaWartosc = np.random.randint(X,Y,1)
#     osX = x['actor_1_facebook_likes'].head(8)
#     plt.xlabel("actor_1_facebook_likes")
#     plt.ylabel("actor_3_facebook_likes")
#     osY = x['actor_3_facebook_likes'].head(8)
#     osX = osX*LosowaWartosc
#     osY = osY*LosowaWartosc
#     #ilosc = osX.count()
#     color = np.random.randint(X,X*3,8)
#     size = np.random.randint(X,X+Z,8)
#     plt.scatter(osX,osY,c=color,s=size)


#     plt.subplot(3,3,9)
#     plt.title("Udzial rezysera")
#     iloscFilmow = x[['director_name','movie_title']].head(8)
#     iloscFilmow = iloscFilmow.groupby(by='director_name').count()
#     print(iloscFilmow)
#     plt.pie(iloscFilmow,autopct="%1.1f%%",labels=iloscFilmow.index.values,shadow=True)
#     plt.legend(bbox_to_anchor=(2.3, 1.05))
#     plt.show()

# wykres(x)




