#Ex 1 - Faça um Programa que peça os três lados de um triângulo.
# O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno

a = int(input(f'Digite o valor do primeiro lado do triângulo: '))
b = int(input(f'Digite o valor do segundo lado do triângulo: '))
c = int(input(f'Digite o valor do terceiro lado do triângulo: '))
print()
if a + b < c or a + c < b or b + c < a or c + a < b:
    print('Não é possível formar um triângulo com esses valores')
elif a == b and c:
    print('Seu triangulo é do tipo Equilátero')
elif a == b or a == c or b == c:
    print('Seu triângulo é do tipo Isóceles')
else:
    print('Seu triângulo é do tipo Escaleno ')


