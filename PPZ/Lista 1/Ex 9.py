#Ex 9 - Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário
# assim como a quantidade de dias pelos quais o carro foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

dist = int(input(f'Quantos Km foram percorridos: '))
dias = int(input(f'Quantos dias o carro ficou alugado: '))

print(f'O valor total do aluguel é: {(dias * 60) + (dist * 0.15)}R$')


