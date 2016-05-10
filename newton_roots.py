# ilustra o processo de newton-raphson
def newtonRaphson(f,flinha,x0,eps=0.0001):
    '''executa o procedimento de newton'''
    a=x0
    b= a - (f(a)/flinha(a))
    k=1 #quero contar as iteracoes
    print("| k | x_k       | |x_k-xk-1|   |")
    print("|{0:<2} | {1:<2.7f} | {2:<2.7f}".format(k,b,abs(b-a)))
  
    while (abs(b-a)>eps):
        a=b
        b= a - (f(a)/flinha(a))
        k+=1
        print("|{0:<2} | {1:<2.7f} | {2:<2.7f}".format(k,b,abs(b-a)))
       
    return b
## funcao de teste
#f = lambda x: x**2-2
#flinha = lambda x: 2*x
#x0=1.5
#newtonRaphson(f,flinha,x0)


## funcao de teste
#f = lambda x: 3*x**3+x**2-x-1
#flinha = lambda x: 9*x**2+2*x-1
#x0=-5.0
#newtonRaphson(f,flinha,x0)

## funcao de teste
#f = lambda x: 2*x**5 -3*x**4 -4*x**3 +x +1
#flinha = lambda x: 10*x**4 -12*x**3 -12*x**3 +1
#x0=3.0
#newtonRaphson(f,flinha,x0)

# funcao de teste
f = lambda x: x**3 +2*x**2 -x -2
flinha = lambda x: 3*x**2 +4*x -x -2
x0=0.5
newtonRaphson(f,flinha,x0)
