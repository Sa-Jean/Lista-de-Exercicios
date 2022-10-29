#Ex 2 - Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os
# números ímpares na lista IMPAR. Imprima as três listas.
import random

lista = random.sample(range(100), 20)
par = []
impar = []
for item in lista:
    if item % 2 == 0:
        par.append(item)
    else:
        impar.append(item)

print(lista)
print(par)
print(impar)
