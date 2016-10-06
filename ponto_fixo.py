# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 15:55:27 2016

@author: buriol
"""
import math

# Método das aproximações sucessivas (ou ponto fixo)
#-------------------------------
phi = lambda x: math.log(x)+2
#phi = lambda x: math.cos(x)

#-------------------------------
x0 = 3.3
eps = 0.000001
#-------------------------------

# Apenas inicializandoas variáveis
err = 10.0
x_ant = x0
i = 0

while err>eps:
    x = phi(x_ant)
    err = abs(x-x_ant)/abs(x)
    x_ant = x
    i=i+1
    print i, "| x=%.9f"%x, "| err=%.9f"%err
   