#Ex 3 - Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a
# população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B,
# mantidas as taxas de crescimento

A = 80000
B = 200000
anos = int()
while A <= B:
    A = A * (1.03)
    B = B * (1.015)
    anos = anos + 1
else:
    print(f'Levará {anos} anos para que a população de A ultrapasse ou iguale a população de B')
    print(f'Cidade A: {A: .2f}')
    print(f'Cidade B: {B: .2f}')

