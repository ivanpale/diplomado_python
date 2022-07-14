# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 14:25:03 2022

@author: ivann
"""

import pandas as pd

my_data = {"nombre":["jhonier","pablo","ana","wendy","andres","sesana","elena","ivan"],
           "edad":[19, 20, 20, 22, 21, 23, 24, 18, 20, 21],
           "sexo":["masculino", "masculino","femenino","femenino","masculino","femenini","femenino","masculino"],
           "peso":[67, 57, 65, 59, 60, 55, 63, 67],
           "altura":[1.85,1.63,1.55,1.56,1.45,1.72,1.59,1.95],
           "dinero a invertir":[10000,200000,250000,150000,170000,210000,300000,190000],
           "interes":[10,15,25,5,16,30,21,13],
           "años de inversion":[1, 2, 3, 3, 2, 1, 4, 5],
           "telefono":[1234567891,5547236847,5489376598,5427356567,5483254734,6593846589,4465346956,5464736589],
           "compra de pan":[3,4,7,8,2,7,5,1]
          
}
                     
peso = input("¿Cuál es tu peso en kg? ")
altura = input("¿Cuál es tu altura en metros?")
imc = round(float(peso)/float(estatura)**2,2)
print("Tu índice de masa corporal es " + str(imc))

amount = float(input("dinero a invertir "))
interest = float(input("¿Interés porcentual anual? "))
years = int(input("¿Años?"))
print("Capital final: " + str(round(amount * (interest / 100 + 1) ** years, 2)))


barras = int(input("Introduce el número de barras vendidas que no son frescas: "))
precio = 3.49 
descuento = 0.6
coste = barras * precio * (1 - descuento)
print("El coste de una barra fresca es " + str(precio) + "€")
print("El descuento sobre una barra no fresca es " + str(descuento * 100) + "%")
print("El coste final a pagar es " + str(round(coste, 2)) + "€")