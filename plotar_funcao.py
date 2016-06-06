# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 00:26:39 2016
@author: buriol

Exemplo de como plotar uma função usando matplotlib (http://matplotlib.org)
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2*3.1415, 0.1); # Cria os valores para x 
y = np.sin(x)                    

plt.plot(x, y)
plt.show()