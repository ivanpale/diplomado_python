# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 22:30:42 2022

@author: ivann
"""

# IVAN DARIO PALENCIA ALEAN
# ID: 502223


from sklearn import linear_model 
from scipy import stats
import pandas as pd
import numpy as np


class Regrecion():

    cars_df= pd.read_csv('cars.csv')
    buscado=[]
    condicion=[]
    predicion_Car=0
    
#predecir la producion de co2 segun el volumen del motor y peso del carro
    def PredicionCO2(self,volumen, peso):
    
        x= self.cars_df[['Volume','Weight']]
        y = self.cars_df['CO2']
        
        x1= np.array(x)
        y1= np.array(y)
        
        reg_mod = linear_model.LinearRegression()
        reg_mod.fit(x1,y1)
        
        predic_co2 = reg_mod.predict([[volumen,peso]])
        
        print(predic_co2)
        
        print(reg_mod.coef_)
        
        
# variable de salida reemplazando los strings por números respectivos
    def Etiquetar_Numerica_Car(self):
               
        marcas=self.cars_df["Car"]

        for dato in  marcas:

            if self.buscado.count(dato) == 0 :
                self.buscado.append(dato)

        etiqueta = range(len(self.buscado))
    
        
        for dato_marca in self.buscado :
                
            self.condicion.append((self.cars_df["Car"]== dato_marca))
            
        self.cars_df["Car"]= np.select(self.condicion,etiqueta)
        
        
    # metodo que permite a partir de los valores independientes (volumen, peso y producción de CO2) predecir el comportamiento de la variable dependiente (marca del carro.)
    def Predicion_Car(self, x, y ,volumen,peso,co2):
        
        
        x1= np.array(x)
        y1= np.array(y)
        
        reg_mod = linear_model.LinearRegression()
        reg_mod.fit(x1,y1)
        
        predic_Car = reg_mod.predict([[volumen,peso,co2]])
        self.predicion_Car= round(predic_Car[0])
        
        print(predic_Car)
        
        print(reg_mod.coef_)
        
        
    def Valor_r(self,Volume, Weight, Co2, Car):
        
        slope,intercept,r,p,std_err = stats.linregress(Volume, Car)
        slope1,intercept1,r_1,p1,std_err1 = stats.linregress(Weight, Car)
        slope2,intercept2,r_2,p2,std_err2 = stats.linregress(Co2, Car)
    
        return r,r_1,r_2
        
       


Predicion = Regrecion()
print ("------------Predicion  CO2------------\n")
Predicion.PredicionCO2(1300,2300)
Predicion.Etiquetar_Numerica_Car()


print ("------------Predicion  CO2------------\n")
x=Predicion.cars_df[['Volume','Weight','CO2']]
y=Predicion.cars_df['Car']
Predicion.Predicion_Car(x,y,1300,2000,107.20)


print ("----------Marca predecida----------\n")

print (Predicion.buscado[Predicion.predicion_Car])


print ("--------------Valor de los R------------\n")

volume1=list(Predicion.cars_df['Volume'])
weight1=list(Predicion.cars_df['Weight'])
co21=list(Predicion.cars_df['CO2'])
car1=list(Predicion.cars_df['Car'])
r,r_1,r_2=Predicion.Valor_r(volume1,weight1,co21,car1)
print ("R de correlacion de la variable Volume con Car:  " + str(r))
print("R de correlacion de la variable Weight con Car:  " + str(r_1))
print("R de correlacion de la variable CO2 con Car:  " + str(r_2))


print ("------------------------Promedio de  R--------------------------------------\n")
print( "Promedio de R :" + str(np.median(Predicion.Valor_r(volume1,weight1,co21,car1))))