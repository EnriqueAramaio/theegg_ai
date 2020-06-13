# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 14:28:06 2020

@author: enriq
"""


a=float(input()) # para introducir el numero solicitado del problema
x=round(float(1),4) #Variable para calculo de ecuacion
y=round((x/a),4) #Variable ecuacion


while x/y!=a:
    x+=1
    y=round((x/a),4)
    #print(y)
print(int(x),'/',int(y))