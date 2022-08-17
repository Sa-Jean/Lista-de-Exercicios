#Ex 4 - Faça um Programa que leia três números e mostre o maior deles.

a = int(input('Digite um numero: '))
b = int(input('Digite um numero: '))
c = int(input('Digite um numero: '))

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)

