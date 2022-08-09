#Ex 5 - Solicite o preço de uma mercadoria e o percentual de desconto.
# Exiba o valor do desconto e o preço a pagar

p = int(input('Digite o valor da mercadoria: '))
d = int(input('Digite quantos % de desconto: '))
print()
print(f'O valor do desconto é: {p * (d/100) }R$')
print(f'O valor final é: {p - p * (d/100)}R$')