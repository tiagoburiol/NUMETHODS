# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 17:40:47 2016

@author: buriol
"""
import math 

# Método da bisseção
#-------------------------------
f = lambda x: x**2 + math.log(x)
#f = lambda x: math.log(x)-math.sin(x)
#-------------------------------
a =0.10
b = 1.0
eps = 0.01
#-------------------------------

# Apenas inicializando
err = 10.0
amp = 10.0
x_ant = a
i = 0

n_max = (math.log10(b-a) - math.log10(eps))/math.log10(2)
print "Estimativa do número de iterações: ", n_max

while err>eps or err>amp:
    xm = (a+b)/2.0
    if f(xm)*f(a)<0:
        b = xm
    else:
        a = xm
    amp = (b-a)/2.0    
    err = abs((xm-x_ant)/xm)
    x_ant = xm
    i=i+1
    print i, "| xm=%.5f"%xm, "| f(a)=%.5f"%f(a), "| f(xm)=%.5f"%f(xm) , "| f(b)=%.5f"%f(b),"| err=%.5f"%err,"| amp=%.5f"%amp
    