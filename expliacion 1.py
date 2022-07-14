# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 10:23:29 2022

@author: ivann
"""

import matplotlib.pyplot as plt
from scipy import stats

# x es edades y y es velocidad
x=[5,7,8,7,2,17,2,9,4,11,12,9,6]
y=[99,86,87,88,111,86,103,87,94,78,77,85,86]

#diagrama de dispersion de los datos
plt.scatter(x, y, )
#plt.show()
#labels del plt y titulo
plt.xlabel("Años que tiene el carro")
plt.ylabel("velocidad alcanzada")
plt.title("velocidad vs Años")


#variables estadisticas returnadas del metodo lingress
slope, intercept,r,p,std_err = stats.linregress(x,y)

#crear una funcion para crear la linea linfress
def regresion(x):
    return slope*x+intercept

regre_model = list(map(regresion, x))

plt.plot(x,regre_model)
plt.show()


#prediccion par un vehiculo de 10 años 
speed = regresion(10)
print(speed)


















