#Ex 3 - Escreva um programa que leia a quantidade de dias, horas,minutos e segundos do usuário.
# Calcule o total em segundos

d = int(input('Digite um valor em dias: '))
h = int(input('Digite um valor em horas: '))
m = int(input('Digite um valor em minutos: '))
s = int(input('Digite um valor em segundos: '))

print(f'O Valor total em segundos é: {d*86400 + h * 3600 + m * 60 + s}')