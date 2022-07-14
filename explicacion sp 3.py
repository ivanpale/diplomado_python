# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 11:38:41 2022

@author: ivann
"""
#impor librerias
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score

#definir la variables x y y
#x son las horas
#y son las velocidades

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

#diagrama de dispersion
plt.scatter(x,y)
plt.show()

#modelo polinomial
poli_model = np.poly1d(np.polyfit(x, y, 5))


#R
print(r2_score(y,poli_model(x)))


#definimos el espacionamiento para la linea
poli_line = np.linspace(1, 22, 100)

#nuevos valores de y
poli_new_y = poli_model(poli_line)

#dibujamos la linea de regresion polinomial
plt.plot(poli_line, poli_new_y)
plt.show()

#imprimir la forma del polinomio
print(poli_model)

#predecir valor y de la velocidad
speed_pred = poli_model(17)
print(speed_pred)

