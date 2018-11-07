# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 14:46:34 2017

@author: buriol
"""
import matplotlib.pyplot as plt
import numpy as np

x = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
#print (x)
#print (len(x))


u = np.empty(6)
print (u)
n = 5

u_ant = np.ones(6)
print (u_ant)
U = [u_ant]

for i in range(1,100,1):
    u[0] = 0.
    for j in range(1,n,1):
        u[j] = 0.5*u_ant[j] + 0.25*(u_ant[j+1] + u_ant[j-1])
    u[n] = 0.5*u_ant[n] + 0.25*(u_ant[n-1]-0.4*u_ant[n]+u_ant[n-1])
    u_ant = u.copy()
    U.append(u_ant)
    
    print (i, u)
    
#print (U)
plt.plot(x, U[10], x, U[50], x, U[99])
plt.show()