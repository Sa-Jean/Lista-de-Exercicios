#Ex 4 - Faça um programa que calcule o aumento de um salário.
# Ele deve solicitar o valor do salário e a porcentagem do aumento.

s = int(input('Digite o valor do seu Salário: '))
a = int(input('Digite a porcetagem do seu aumento: '))

print(f'Valor do seu aumento é: {s * (a/100): .2f}R$')
print(f'Seu novo salário é: {s + (s *(a/100)): .2f}R$')