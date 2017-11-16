
"""
Created on Mon Nov 13 20:09:13 2017

@author: buriol
"""
## module newtonPoly
'''p = evalPoly(a,xData,x).
Evaluates Newton’s polynomial p at x. The coefficient
vector {a} can be computed by the function ’coeffts’.
a = coeffts(xData,yData).
Computes the coefficients of Newton’s polynomial.
'''

#ççç
import numpy as np
xData = np.array([0.15, 0.17, 0.19, 0.21, 0.23, 0.25, 0.27, 0.29, 0.31])
yData = np.array([0.1761, 0.2304, 0.2788, 0.3222, 0.3617, 0.3979, 0.4314, 0.4624, 0.4914])


def evalPoly(a,xData,x):
    n = len(xData) - 1
    # Degree of polynomial
    p = a[n]
    for k in range(1,n+1):
        p = a[n-k] + (x -xData[n-k])*p
    return p

def coeffts(xData,yData):
    m = len(xData)
    # Number of data points
    a = yData.copy()

    for k in range(1,m):
        a[k:m] = (a[k:m] - a[k-1])/(xData[k:m] - xData[k-1])
    return a


a = coeffts(xData,yData)


#Xplot = np.linspace(xData[0], xData[-1], 21)
#Yplot = []
#Yplot2 = []
#for x in Xplot:
#    Yplot.append(evalPoly(a,xData,x))
#    #Yplot.append(calculaP(x))
#    #Yplot2.append(calculaP2(x))
#    #print calculaP(x)-calculaP2(x)
#plt.plot(xData, yData, "ro", Xplot, Yplot, "-")

#plt.plot(X, Y, "ro", Xplot, Yplot, "-",Xplot, Yplot2, "-") 
#plt.show()