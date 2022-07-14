# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 22:00:31 2022

@author: ivann
"""
# IVAN DARIO PALENCIA ALEAN
# ID: 502223


import pandas as pd
import numpy as np 

class persona():

    Datos_estudiantes = {"Nombre":["JESUS","DEIVER","ENA","WENDY","IVAN"],
                         "Edade" :[25,20,19,23,21],
                         "Sexo" :["M","M","F","F","M"],
                         "Peso KG" :[85,70,60,65,65],
                         "Altura M":[ 1.78,1.70,1.60,1.65,1.75],
                         "Dinero a invertir ":[1000000,2000000,3000000,3500000,400000],
                         "Interes anual":[0.12,0.20,0.9,0.13,0.10],
                         "Años de inversion":[2,1,3,10,5],
                         "Numero telefonico":["+57-3023449991","+57-3205178529","+57-3015712028","+57-3012695219","+57-3225033505"],
                         "Hora de compra del pan":[20,1,17,9,4]
                          }

# el diccionario se convierte en un dataframe 
    datos = pd.DataFrame(Datos_estudiantes)
    
        
#parte_1

# calcular el indice de masa corporal
    def calcular_imc(self):
    
# formula imc
        self.datos["imc"]=self.datos["Peso KG"]/self.datos["Altura M"]**2
        
   
 
        for inicio in self.datos["imc"]:
             print ("Tu índice de masa corporales es  "+str(round(inicio,2))+" donde 18.5—24.9 es el índice de masa corporal normal \n")
             
        
        
#parte_2 
 
    def ganancias_invercion(self):
        
        capital_final=0.0
        capital_final=self.datos["Dinero a invertir "] *(self.datos["Interes anual"]/100+1)**self.datos["Años de inversion"]
        self.datos["capital final"]= capital_final
        return capital_final
    
#parte_3
        
    
    def Descuento_Pan(self):
        
        condicion=[
                   (self.datos["Hora de compra del pan"]<= 6),
                   (self.datos["Hora de compra del pan"]> 6)&(self.datos["Hora de compra del pan"]<= 12),
                   (self.datos["Hora de compra del pan"]> 12)&(self.datos["Hora de compra del pan"]<= 18),
                   (self.datos["Hora de compra del pan"]> 18)&(self.datos["Hora de compra del pan"]<= 24)
                  
                  
                   ]
     
        opcion =[0.10,
                 0.20,
                 0.30,
                 0.40
                ]
        
        self.datos["descuento"]= np.select(condicion,opcion)
    
    # metodo que permite calcular el valor de cada pan segun el descuento obtenido anterior mente el metodo anterior  
    def Precio_Pan(self):
        
        self.datos["Precio del Pan"]= 15000-(self.datos["descuento"]*15000)
        
#parte_4
        

    def Extencion_Num_Celular(self):
        
        self.datos["Numero Telefonico extencion"]= np.where(self.datos["Sexo"]=="M",self.datos["Numero telefonico"]+"-11",self.datos["Numero telefonico"]+"-10")
        
        



obj_persona= persona()

obj_persona.calcular_imc()
print (obj_persona.ganancias_invercion())
obj_persona.Descuento_Pan()
obj_persona.Precio_Pan()
obj_persona.Extencion_Num_Celular()
print("tabla de datos ")
print(obj_persona.datos)
