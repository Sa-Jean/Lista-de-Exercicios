#Ex 6 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS,
# quanto pagou ao sindicato e o salário líquido.
# Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os
# descontos e o salário líquido, conforme a tabela abaixo:
#a. + Salário Bruto : R$
#b. - IR (11%) : R$
#c. - INSS (8%) : R$
#d. - Sindicato ( 5%) : R$
#e. = Salário Liquido : R$

h = int(input('Quanto você recebe por hora trabalhada: '))
t = int(input('Quantas horas trabalha por mês: '))
sb = h * t
IR = sb * (11/100)
INSS = sb * (8/100)
Sindicato = sb * (5/100)
print(f'Salário Bruto: {sb}R$')
print(f'IR: {IR}R$')
print(f'INSS: {INSS}R$')
print(f'Sindicato: {Sindicato}R$')
print(f'Salário Liquido: {sb - IR - INSS - Sindicato }R$')



