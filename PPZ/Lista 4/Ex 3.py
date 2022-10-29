#Ex 3 - Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um terceiro
# vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
# Imprima os três vetores.
import random

vet1 = random.sample(range(100), 10)
vet2 = random.sample(range(100), 10)
vet3 = []

for indice in range(10):
    vet3.append(vet1[indice]),vet3.append(vet2[indice])


print(vet1)
print(vet2)
print(vet3)


