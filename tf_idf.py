import pandas as pd
from itertools import combinations
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Definimos nuestro archivo
movies_file = "Data_pelicula.csv"

#Leemos el archivo
movies = pd.read_csv(movies_file, sep=';', encoding='UTF-8')

##Se construye la matriz TD-IDF
"""
Se quiere hallar el conjunto de combinaciones de géneros
mayor a cuatro. En términos matemáticos, se quiero hallar el subconjunto.
    """
tf = TfidfVectorizer(analyzer=lambda s: (c for i in range(1,4)
                                             for c in combinations(s.split(', '), r=i)))
tfidf_matrix = tf.fit_transform(movies['Genero_Pelicula'])
tfidf_matrix.shape

#Esta es la matriz TD-IDF, el subconjunto buscado.
pd.DataFrame(tfidf_matrix.todense(), columns=tf.get_feature_names_out(), index=movies.Titulo_original).sample(5, axis=1).sample(10, axis=0)

##Se calcula la similitud del coseno usando la matriz TD-IDF
cosine_sim = cosine_similarity(tfidf_matrix)

## Se crea dataframe de similitud
"""
Esto al final genera una matriz cuadrada, con la intención de comprobar
la similitud entre las películas. Si la similitud es 1, significa que las películas tienen el mismo género.
Mientras el valor del ángulo sea más cercano a 1, las películas tendrán mayor similtud.
    """
cosine_sim_df = pd.DataFrame(cosine_sim, index=movies['Titulo_original'], columns=movies['Titulo_original'])
print('Shape:', cosine_sim_df.shape)
cosine_sim_df.sample(5, axis=1).round(2)

#Función de recomendación por género
def genre_recommendations(i, k=20):
    """
    Recomendar películas en base a las similitudes del dataframe 
    Parámetros
    ----------
    i : str
        Película (index of the similarity dataframe)
    M : pd.DataFrame
        Similitud en el dataframe, simetría dentro del dataframe con las películas como filas y columnas 
    items : pd.DataFrame
        Contiene el título y algunas otras características usadas para definir la similitud.
    k : int
        Número de recomendaciones a retornar.
    """
    M= cosine_sim_df ## Se define la matriz de similitud
    items= movies[['Id_Pelicula','Titulo_original','Fecha_estreno','Descripcion','Cartel_path','Genero_Pelicula']]
    ix = M.loc[:,i].to_numpy().argpartition(range(-1,-k,-1))
    closest = M.columns[ix[-1:-(k+2):-1]] ## Se seleccionan las k películas más cercanas
    closest = pd.DataFrame(closest)  ## Se convierte a DataFrame
    closest = closest.sample(k)  ## Se seleccionan k películas en orden aleatorio.
    closest = closest[closest != i] ## Se excluye la película de referencia
    return pd.DataFrame(closest).merge(items).head(5) ## Se retorna el resultado de las primeras 5 películas de la lista.
