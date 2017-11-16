# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 14:12:40 2016

@author: buriol
"""
import matplotlib.pyplot as plt
import numpy as np

X = [0.15, 0.17, 0.19, 0.21, 0.23, 0.25, 0.27, 0.29, 0.31]
Y = [0.1761, 0.2304, 0.2788, 0.3222, 0.3617, 0.3979, 0.4314, 0.4624, 0.4914]

dd = []    # Cria uma lista vazia para armazenar as diferencas divididas

# Inserindo na lista de diferencas divididas a lista de dif. div. de ordem 0 
dd.append(Y) 
# ...imprimindo para conferir     
#print (dd[0])

# Gerando a tabela de diferecas divididas a partir da ordem 1 em diante
for ordem in range(1, len(X), 1):
    dd.append([])   # Adiciona uma lista vazia para armazenar as dds de ordem 1
    
    # Para cada ordem, calcula a lista de valores resultantes
    for k in range(0, len(X)-ordem, 1): 
        #print (ordem, k)
        #print (dd[ordem-1][k+1],dd[ordem-1][k],x[k+ordem], x[k]) 
        valor = (dd[ordem-1][k+1]-dd[ordem-1][k])/(X[k+ordem]-X[k])    
        #print (valor)        
        dd[ordem].append(valor)
    #print (dd[ordem])



def produtorio(x,n):
    prod = 1.
    for i in range(n):
        prod = prod * (x-X[i])
    return prod


def calculaP(x):
    soma = dd[0][0]
    for i in range(1,len(X)):
        soma = soma + produtorio(x,i)*dd[i][0]
    return soma



def calculaP2(x):
    valor = 0
    for k in range(len(Y)):
        lk = 1.0
        for i in range(len(X)):
            if k != i:
                lk = lk*(x - X[i])/(X[k]-X[i])
        valor = valor +Y[k]*lk 
    return valor



Xplot = np.linspace(X[0], X[-1], 21)
Yplot = []
Yplot2 = []
for x in Xplot:
    Yplot.append(calculaP(x))
    Yplot2.append(calculaP2(x))
    print calculaP(x)-calculaP2(x)


plt.plot(X, Y, "ro", Xplot, Yplot, "-",Xplot, Yplot2, "-") 
plt.show()

