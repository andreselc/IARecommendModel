import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Definimos nuestro archivo

movies_file = "Data_pelicula.csv"
users_file = "users.csv"
ratings_file = "ratings.csv"

#Leemos el archivo
movies = pd.read_csv(movies_file, sep=';', encoding='UTF-8')

s = "Action Drama Adventure"
tf_wrong = TfidfVectorizer(analyzer='word', ngram_range=(1,2))
tf_wrong.fit([s])
tf_wrong.get_feature_names_out()
[c for i in range(1,2) for c in combinations(s.split(), r=i)]

tf = TfidfVectorizer(analyzer=lambda s: (c for i in range(1,4)
                                             for c in combinations(s.split(', '), r=i)))
tfidf_matrix = tf.fit_transform(movies['Genero_Pelicula'])
tfidf_matrix.shape

pd.DataFrame(tfidf_matrix.todense(), columns=tf.get_feature_names_out(), index=movies.Titulo_original).sample(5, axis=1).sample(10, axis=0)

cosine_sim = cosine_similarity(tfidf_matrix)

cosine_sim_df = pd.DataFrame(cosine_sim, index=movies['Titulo_original'], columns=movies['Titulo_original'])
print('Shape:', cosine_sim_df.shape)
cosine_sim_df.sample(5, axis=1).round(2)

def genre_recommendations(i, k=5):
    """
    Recommends movies based on a similarity dataframe

    Parameters
    ----------
    i : str
        Movie (index of the similarity dataframe)
    M : pd.DataFrame
        Similarity dataframe, symmetric, with movies as indices and columns
    items : pd.DataFrame
        Contains both the title and some other features used to define similarity
    k : int
        Amount of recommendations to return

    """
    M= cosine_sim_df
    items= movies[['Titulo_original','Fecha_estreno','Descripcion','Cartel_path','Genero_Pelicula']]
    ix = M.loc[:,i].to_numpy().argpartition(range(-1,-k,-1))
    closest = M.columns[ix[-1:-(k+2):-1]]
    closest = closest.drop(i, errors='ignore')
    return pd.DataFrame(closest).merge(items).head(k)
