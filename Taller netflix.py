# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 21:41:57 2022

@author: ivann
"""
# IVAN DARIO PALENCIA ALEAN
# ID: 502223


import pandas as pd 

my_nexflix = pd.read_csv('netflix_titles.csv')
my_nexflix


print(my_nexflix.head(5))
print(my_nexflix.tail(5))

print(my_nexflix.dtypes)


my_nexflix.to_excel("Netflix_list.xlsx", sheet_name="títulos", index=False)

#se crea una nueva data frame en el cual segmente únicamente: el tipo, la duración, la descripción y el país.

new_data_nexflix = my_nexflix.loc[:,['type','duration','description','country']]

# filtro para las películas que tienen una duración superior a 100 min.

my_nexflix["duration_minutos"] = pd.to_numeric(my_nexflix['duration'].replace('([^0-9]*)','', regex=True), errors='coerce')
filtro_100m= my_nexflix[my_nexflix["duration_minutos"] > 100]

#filtro para los “TV Shows” que tienen más de 3 temporadas.
filtro_Tv_shows= my_nexflix[my_nexflix["type"] == "TV Show"]

# filtro en el cual solo cuenta con 2 categorías/etiquetas
categorias = my_nexflix.loc[my_nexflix['country'].isin(['India','Germany, Czech Republic'])]


# Modificacion de los valores del ID de las 5 primeras y las 5 últimas “shows” 
my_nexflix.iloc[:5,0]='s10'

my_nexflix.iloc[8802:,0]='s1'