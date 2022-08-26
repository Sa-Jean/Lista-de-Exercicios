#Ex 5 - Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando o algoritmo de Euclides


a = int(input("Digite um numero: "))
b = int(input("Digite um numero: "))

while a % b != 0:
    a, b = b, a % b

print(f'O Máximo divisor comun entre eles é: {b}')
