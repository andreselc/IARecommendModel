# TF-IDF

Este es el repositorio que contiene el modelo de machine learning para recomendar películas según la interacción que se tenga con la aplicación (likes a las películas). El algoritmo que se usa para recomendar películas es el TF-IDF.

-TF: Frecuencia del Término. 
Mientras mayor sea la frecuencia del término en los documentos, mayor será su importancia.

-IDF: Frecuencia inversa de documentos
Mientras mayor sea la frecuencia del término en los documentos, menor será su importancia. 

Este es un cálculo estadístico adoptado por el algoritmo de Google para medir cuáles términos son más relevantes para el usuario, analizando la frecuencia de las páginas con las que interactúan junto con la frecuencia en un conjunto más grande de páginas.

Como ya se sabe, no solo se usa en motores de búsquedas de internet, también se usa en sistemas bibliotecarios, en minería de datos, entre otras áreas.

## ¿Cómo funciona el proyecto?

Se utilizó Flask para definir una API sencilla que recibiera una solicitud de la API definida en .NET, cuando el endpoint que recomienda películas se ejecute. 

El código está diseñado para recomendar películas basadas en la similitud de género entre películas y lo hace de la siguiente manera:

-Vector tf-idf:

Funciona para textos, sin embargo, posee propiedades que son útiles para este proyecto, en orden de obtener un vector que represente la data que se necesita.

El cálculo del IDF considera qué términos se repiten frecuentemente en los textos, como artículos y conjunciones (el, la, lo, y, pero, que, etc.), y no tienen relevancia para los documentos. Cuando el factor IDF se incorpora dentro de la fórmula (que será mostrada más adelante), el cálculo disminuye el peso de los términos que ocurren con mucha frecuencia en el conjunto de documentos y aumenta el peso de los términos que aparecen más raramente.

La expresión que explica lo anterior, es la que se muestra a continuación:

![Expresión TDF-IDF](IARECOMMEND/images/IDFormula.png)

Siendo: 

tf: Número total de ocurrencias de i en j.
df: Número total de documentos (discursos) que contienen i.
N: Número total de documentos (discursos).
tf,j: Frecuencia de la palabra clave i en el documento j.
log: Logaritmo neperiano.


## Instalación


# Opcional:


# Diseño y Arquitectura:

# Referencias Bibliográficas y Librerías:



## Liberías y dependencias utilizadas:



    

