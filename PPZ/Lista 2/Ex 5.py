#Ex 5 - Faça um Programa que leia três números e mostre o maior e o menor deles.

a = int(input('Digite um numero: '))
b = int(input('Digite um numero: '))
c = int(input('Digite um numero: '))

if a > b and a > c:
    print(f'O maior numero é: {a}')
elif b > a and b > c:
    print(f'O maior numero é: {b}')
else:
    print(f'O maior numero é: {c}')
if a < b and a < c:
    print(f'O menor numero é: {a}')
elif b < a and b < c:
    print(f'O menor numero é: {b}')
else:
    print(f'O menor numero é: {c}')

