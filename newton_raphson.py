# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 15:55:27 2016

@author: buriol
"""
import math

# Método de Newton-Raphson
#-------------------------------
f = lambda x: 2*x-math.exp(-x)
df = lambda x: 2+math.exp(-x) 
#-------------------------------
x0 = 0.4
eps = 0.00001
#-------------------------------

# Apenas inicializandoas variáveis
err = 10.0
x_ant = x0
i = 0

while err>eps:
    x = x_ant-f(x_ant)/df(x_ant)    
    err = abs(x-x_ant)
    x_ant = x
    i=i+1
    print i, "| x=%.9f"%x, "| err=%.9f"%err
   