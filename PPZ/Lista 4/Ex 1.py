#Ex 1 - Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar
# as funções max, min e short.

import random

k = 0
x = random.sample(range(100), 10)
maior = x[0]
menor = x[0]
for k in x:
    if k > maior:
        maior = k
    elif k < menor:
        menor = k

print(x)
print(maior)
print(menor)

