#Ex 7 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
# ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
# em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
# Obs. : somente são vendidos um número inteiro de latas

t = int(input('Qual tamanho da area a ser pintada em Metros Quadrados: '))
l = 54 #metros que podem pintar

resto = t % l
c = t // l
if resto == 0:
    print(f'Você precisará comprar: {c} Latas de tinta')
    print(f'Valor total: {c * 80: .2f}R$')
else:
    print(f'Você precisará comprar: {c+1} Latas de tinta')
    print(f'Valor total: {(c + 1)* 80}R$')
