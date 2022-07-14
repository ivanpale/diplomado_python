# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 22:42:45 2022

@author: ivann
"""

import pandas as pd
from sklearn import tree 
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt 
import matplotlib.image as pltimg
import pydotplus
import statsmodels.api as sm 
import numpy as np

# Utilizar el set de datos Carseats  y lo convertimo en un Dataframe 
carseats = sm.datasets.get_rdataset("Carseats","ISLR")
datos = carseats.data

# print(carseats.__doc__)
#a partir de la variable Sale se creo una nueva variable dicotómica donde:
# si las ventas son mayores a 8 se cambiara el valor a 0 (ventas altas)
# si las ventas son menores de 8 se cambiara el valor a 1(ventas bajas)
datos['Ventas_Altas']= np.where(datos.Sales > 8,0,1)

# eliminamos la columna Sale 
datos= datos.drop(columns='Sales')


#cambiamos los datos no numericos por una etiqueta numerica que los identifique para poder hacer las respectivas operaciones

# creamos un diccionario con los datos de la columna shelveloc 
d ={'Good':0,'Medium':1,'Bad':2}
#mapeamos los datos del diccionario
datos['ShelveLoc']= datos['ShelveLoc'].map(d)

# creamos un diccionario con los datos de la columna Urban
d ={'Yes':0,'No':1}
#mapeamos los datos del diccionario
datos['Urban']= datos['Urban'].map(d)

# creamos un diccionario con los datos de la columna US
d ={'Yes':0,'No':1} 
#mapeamos los datos del diccionario
datos['US']= datos['US'].map(d)


#creamos na lista de los datos o variables  indepenndientes
feature = ['CompPrice','Income','Advertising','Population','Price','ShelveLoc','Age','Education','Urban','US']

# Creamos nuetra variable x con los valores del datos utilizando las features 
x= datos[feature]
# creamos nuetra variable  y con la columna de destino
y=datos['Ventas_Altas']


#Selecionamos el 80% de los datos con el fin de definir los datos de entrenamiento 
train_x= x[:320]
train_y= y[:320]

# selcionamos el 20% de los datos restantes como datos de prueba 
test_x= x[320:]
test_y= y[320:]

#Creamos nuetro arbol de decision 
dtree= DecisionTreeClassifier()

# se ajustan los datos al modelo utilizando los datos de entrenamiento 
dtree = dtree.fit(train_x,train_y)

# exportar los datos para poderlos graficar en el diagrama de flujo 
data = tree.export_graphviz(dtree, out_file=None, feature_names = feature)
# se crea la grafica 
graph = pydotplus.graph_from_dot_data(data)
# guardamos la grafica como arbol_de_decision_ventas.png
graph.write_png('arbol_de_decision_ventas.png')
# abrir la grafica  y la mostramos por pantalla 
img = pltimg.imread('arbol_de_decision_ventas.png')
imgplot = plt.imshow(img)
plt.show()


#vamos a hacer la prediccion con los datos que obtubimos en los datos de prueba


data_prediccion= np.array(test_x)
print("\n")
print ("CompPrice: "+str(data_prediccion[0][0]))
print ("Icome: "+str(data_prediccion[0][1]))
print ("Advertissing: "+str(data_prediccion[0][2]))
print ("Population: "+str(data_prediccion[0][3]))
print ("Price: "+str(data_prediccion[0][4]))
print ("ShelveLoc: "+str(data_prediccion[0][5]))
print ("Age: "+str(data_prediccion[0][6]))
print ("Education: "+str(data_prediccion[0][7]))
print ("Urban: "+str(data_prediccion[0][8]))
print ("US: "+str(data_prediccion[0][9])+"\n")

print ("Prediccion")
print (dtree.predict([[data_prediccion[0][0],data_prediccion[0][1],data_prediccion[0][2],data_prediccion[0][3],data_prediccion[0][4],data_prediccion[0][5],data_prediccion[0][6],data_prediccion[0][7],data_prediccion[0][8],data_prediccion[0][9]]]))


#imprime la ayuda para las respuestas

print ("[1] mean 'Ventas Altas'")
print ("[0] mean 'Ventas Bajas'")
