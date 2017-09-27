
# Trabalho 1

### Questão 1
Pesquise e responda: O que é o 'Épsilon da Máquina'? Apresente um programa em python para obter o épsilon do computador que você usa. Qual o valor obtido com seu programa?  

**Resolução**


```python
eps=1

while (eps+1) > 1:
    eps = eps/2

print ("Epsilon:", eps*2)
```

    Epsilon: 2.220446049250313e-16


**Comentário** <br>
O épsilon da máquina é o menor número que somado a 1 produza resulta dem um número diferente de 1. Representa a exatidão relativa da aritmética de ponto flutuante do computador em uso. Em um PC 64 bits, o épslon resultou no valor 2.220446049250313e-16.

### Questão 2

Considere as expressões 
$ \frac{e^{1/x}}{1+e^{1/x}} $ e   $\frac{1}{e^{-1/x}+1}$ . Verifique que, para x>0, são funções idênticas, então, use um programa em Python para testar o valor de cada uma para alguns valores de x entre 0.1 e 0.001. Qual dessas expressões é mais adequada quando x é um número pequeno? Explique. 

**Resolução**


```python
from math import exp
def f1(x): return exp(1./x)/(1+exp(1./x))
print ("f1(0.1) =", f1(0.1))
print ("f1(0.05) =", f1(0.05))
print ("f1(0.01) =", f1(0.01))
print ("f1(0.005) =", f1(0.005))
print ("f1(0.002) =", f1(0.002))
print ("f1(0.015) =", f1(0.0015))
print ("f1(0.015) =", f1(0.0014))
print ("f1(0.001) =", f1(0.001))
```

    f1(0.1) = 0.9999546021312976
    f1(0.05) = 0.9999999979388464
    f1(0.01) = 1.0
    f1(0.005) = 1.0
    f1(0.002) = 1.0
    f1(0.015) = 1.0



    ---------------------------------------------------------------------------

    OverflowError                             Traceback (most recent call last)

    <ipython-input-5-60ccab6800fe> in <module>()
          7 print ("f1(0.002) =", f1(0.002))
          8 print ("f1(0.015) =", f1(0.0015))
    ----> 9 print ("f1(0.015) =", f1(0.0014))
         10 print ("f1(0.001) =", f1(0.001))


    <ipython-input-5-60ccab6800fe> in f1(x)
          1 from math import exp
    ----> 2 def f1(x): return exp(1./x)/(1+exp(1./x))
          3 print ("f1(0.1) =", f1(0.1))
          4 print ("f1(0.05) =", f1(0.05))
          5 print ("f1(0.01) =", f1(0.01))


    OverflowError: math range error



```python
from math import exp
def f1(x): return 1./(exp(-1./x)+1)
print ("f1(0.1) =", f1(0.1))
print ("f1(0.05) =", f1(0.05))
print ("f1(0.01) =", f1(0.01))
print ("f1(0.005) =", f1(0.005))
print ("f1(0.002) =", f1(0.002))
print ("f1(0.015) =", f1(0.0015))
print ("f1(0.014) =", f1(0.0014))
print ("f1(0.001) =", f1(0.001))
```

    f1(0.1) = 0.9999546021312976
    f1(0.05) = 0.9999999979388463
    f1(0.01) = 1.0
    f1(0.005) = 1.0
    f1(0.002) = 1.0
    f1(0.015) = 1.0
    f1(0.014) = 1.0
    f1(0.001) = 1.0


**Comentário** <br>
Embora as duas expressões sejam idênticas, observando a saída dos códigos acima, percebe-se que para valores menores do que 0.0015 a primeira expressão resulta em um erro de _*Overflow*_ enquanto que a segunda expressão não ocorre o erro. Assim, podemos dizer que a segunda expressão é mais adequada para valores de x pequenos.

### Questão 3
O número $e$ pode ser definido pela série $e = \sum_{n=0}^{\infty}\left(\frac{1}{n!}\right)$. Apresente um programa em Python para obter uma aproximação para $e$ com erro relativo menor que 0.0001 .

**Resolução**


```python
from math import factorial, e
erro = 1.0
soma = 0.0
n = 0.0
while erro>0.0001:
    soma = soma + 1.0/factorial(n)
    erro = abs(e - soma)/abs(e)
    print ("n =",n,",","soma =",soma, 'erro=', erro)
    n = n + 1
```

    n = 0.0 , soma = 1.0 erro= 0.6321205588285577
    n = 1.0 , soma = 2.0 erro= 0.26424111765711533
    n = 2.0 , soma = 2.5 erro= 0.08030139707139415
    n = 3.0 , soma = 2.6666666666666665 erro= 0.018988156876153812
    n = 4.0 , soma = 2.708333333333333 erro= 0.003659846827343768
    n = 5.0 , soma = 2.7166666666666663 erro= 0.0005941848175817597
    n = 6.0 , soma = 2.7180555555555554 erro= 8.324114928800986e-05


**Comentário** <br>
Com seis termos, a série resulta em um valor aproximado de $e$ com erro relativo menor que 0.0001.

### Questão 4
A fórmula de Leibniz para o número $\pi$ é dada pela série infinita $\frac{\pi}{4} = \sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1}$. Apresente um programa em Python para obter uma aproximações para $\pi$ usando 50 termos da série.

**Resolução**


```python
soma = 0.0
for n in range(50):
    soma = soma + ((-1.0)**n)/(2*n + 1)
print ("pi =", 4*soma)
```

    pi = 3.121594652591011


**Comentário** <br>
Mesmo com 50 termos, a série ainda apresenta o valor aproximado com erro na segunda casa decimal.

### Questão 5
Apresente um programa em Python para obter aproximações para o valor da função $f(x) = ln(1 + x)$ usando expansões em séries de Taylor em torno do ponto $x = 0$. Descubra quantos termos da série precisam ser retidos para calcular $ln(0.8)$ com erro absoluto inferior a 0.0001.

**Resolução**

A Série de Taylor em torno de x=0, também chamada de Série de McLaurin, para a função $ln(1+x)$ é dada por $\sum_{n=0}^{\infty}\frac{(-1)^nx^{n+1}}{n+1}$


```python
from math import log
soma = 0.0
erro = 10.0
n = 0.0

while erro>0.0001:
    soma = soma + (-1.0)**n * (-0.2)**(n+1)/(n + 1)
    erro = abs(log(0.8)-soma)/abs(log(0.8))
    n = n + 1    
    print ("Resultado:", soma, ", Erro:", erro) 
```

    Resultado: -0.2 , Erro: 0.1037159764550898
    Resultado: -0.22000000000000003 , Erro: 0.014087574100598712
    Resultado: -0.2226666666666667 , Erro: 0.002137120453333192
    Resultado: -0.22306666666666672 , Erro: 0.00034455240624332016
    Resultado: -0.22313066666666673 , Erro: 5.774151870891082e-05


**Comentário** <br>
Pelo resultado do código acima, os 5 primeiros termos da série são suficientes para a aproximar $ln(0.8)$, ou seja, $ln(1+x)$ com $x = -0.2$, com erro menor que 0.0001. 
