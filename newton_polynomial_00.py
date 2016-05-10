# -*- coding: utf-8 -*-
"""
Created on Fri May  6 01:04:37 2016
@author: buriol
"""
# Importando a biblioteca padrao para funcoes matematicas
# import math
# Funcoes trigonometricas podem ser chamadas fazendo math.cos(x) ou math.sin(x)


import matplotlib.pyplot as plt
import numpy as np

# Definindo a lista de pontos a serem interpolados
x  = [1., 2., 4., 5.]
y  = []    # Cria uma lista vazia para armazenar os valores de yi
dd = []    # Cria uma lista vazia para armazenar as diferencas divididas

# Definindo a função a ser interpolada
#f = lambda x: math.cos(math.sin(x*math.pi))
f = lambda x: 1/x

# Atribuindo os valores de f(xi) na lista de valores yi
for i in range(len(x)):
    y.append(f(x[i]))
# ...imprimindo para conferir 
#print (y)

# Inserindo na lista de diferencas divididas a lista de dif. div. de ordem 0 
dd.append(y) 
# ...imprimindo para conferir     
#print (dd[0])

# Gerando a tabela de diferecas divididas a partir da ordem 1 em diante
for ordem in range(1, len(x), 1):
    dd.append([])   # Adiciona uma lista vazia para armazenar as dds de ordem 1
    
    # Para cada ordem, calcula a lista de valores resultantes
    for k in range(0, len(x)-ordem, 1): 
        #print (ordem, k)
        #print (dd[ordem-1][k+1],dd[ordem-1][k],x[k+ordem], x[k]) 
        valor = (dd[ordem-1][k+1]-dd[ordem-1][k])/(x[k+ordem]-x[k])    
        #print (valor)        
        dd[ordem].append(valor)
       
    print (dd[ordem])
 
 


    

    
    
