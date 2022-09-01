#Ex 3 - Questão C. Entre 1067 e 3627 (inclusive), quantos números são pares e também divisíveis por 7?
# Resposta: 183
x = []
y = []
for numero in range(1067, 3628):
    if numero % 2 == 0:
        x.append(numero)
for numero in x:
    if numero % 7 == 0:
        y.append(numero)
print(len(y))