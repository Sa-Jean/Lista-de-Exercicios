#Ex 3 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de
# seu trabalho.Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do
# estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso.
# Se houver, gravar na variável excesso e na variável multa o valor da multa que João deverá pagar.
# Caso contrário mostrar tais variáveis com o conteúdo ZERO.

p = int(input(f'Digite o peso pescado em KG: '))

if p < 50:
    print('Não pescou em excesso')
    print('Multa: 0')
else:
    print(f'Pescou o excedente de: {p - 50}KG')
    print(f'O valor da multa é: {(p - 50)* 4}R$')