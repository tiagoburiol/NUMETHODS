# Chamando a biblioteca numpy
import numpy as np

# Inserindo a matriz dos coeficientes do sistema Ax = b
A = np.array([[30.0, 10.0], [10.0, 5.0]])

# Inserindo o vetor de termos independentes
b = np.array([-110.02, -35.03])

# Gerando a solucao
x = np.linalg.solve(A, b)

# Inprimindo...
print x
