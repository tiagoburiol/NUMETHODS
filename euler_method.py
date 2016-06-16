import numpy as np
import matplotlib.pyplot as plt
import math

a = 0.0
b = 1.0
n = 4
h = (b-a)/n

y0 = 2.0
y = [y0]


x = np.linspace(a, b, n+1)
#print (x)

# Definindo a funcao y'=f(x,y)
f = lambda x,y: y-x

for i in range(n):
    yi = y[i] + h*f(x[i],y[i])
    y.append(yi)


print np.array(y)

# Solucao analitica
ysol = np.exp(x)+x+1.0
print ysol

plt.plot(x, y, 'o-', x, ysol, 'x-')
plt.show()
