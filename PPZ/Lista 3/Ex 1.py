#Ex 1 - Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
# seja inválido e continue pedindo até que o usuário informe um valor válido.

a = int(input('Digite uma nota entre 0 e 10: '))

while a < 0 or a > 10:
    print('Valor invalido')
    a = int(input('Digite uma nota entre 0 e 10: '))
else:
    print(f'Nota válida: {a}')
