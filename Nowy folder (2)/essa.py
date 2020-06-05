import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
df=pd.read_csv("Nowy folder (2)/movie.csv")
naj=df.dtypes.value_counts().head(1)
naj=naj.index.values
def get_statistical_params(df,naj):
    x=df.select_dtypes(include=naj)
    x=x.describe().T
    print(x)
#get_statistical_params(df,naj)
def add_actor_total_fb_likes(x):
    x['actor_total_fb_likes']=x['actor_1_facebook_likes']+x['actor_2_facebook_likes']+x['actor_3_facebook_likes']
    print(x)
# add_actor_total_fb_likes(df)

def get_min_imdb_score(x):
    x=x.sort_values(by=['imdb_score']).head(10)
    x=x['movie_title']
    x=np.array(x)
    print(x)
#get_min_imdb_score(df)
def get_rows_cols(x,X,Y,Z):
    y=x.iloc[X:Y,::]
    y=y.iloc[::Z+X]
    y=y.iloc[::,::Z]
    print(y)
#get_rows_cols(df,3,22*5,3)
def wykres(x):
    plt.subplot(3,3,1)
    y=x[['duration','movie_title']].head(8)
    y1=y['movie_title']
    y=y['duration']
    plt.xticks(rotation=90)
    plt.bar(y1,y,label="dlugosc filmow")
    plt.legend(title="legenda",bbox_to_anchor=(1, 1.05))
    plt.title("długość filmów")
    

    plt.subplot(3,3,5)
    X=3
    Y=22*5
    Z=3
    losowa=np.random.randint(X,Y,1)
    x2=x['actor_1_facebook_likes'].head(8)*losowa
    plt.xlabel="actor_1_facebook_likes"
    y2=x['actor_3_facebook_likes'].head(8)*losowa
    plt.ylabel="actor_3_facebook_likes"
    color = np.random.randint(X,X*3,8)
    size = np.random.randint(X,X+Z,8)
    plt.scatter(x2,y2,c=color,s=size)

    plt.subplot(3,3,9)
    x3=x[['director_name','movie_title']].head(8)
    x3=x3.groupby(by=['director_name']).count()
    plt.pie(x3,labels=x3.index.values,autopct="%1.1f%%")
    plt.title("udział reżysera")
    plt.legend(bbox_to_anchor=(2.3,1))
    plt.show()

wykres(df)

