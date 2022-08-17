#Ex 10 - Escreva um programa para calcular a redução do tempo de vida de um fumante.
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
# Considere que um fumante perde 10 minutos de vida a cada cigarro.
# calcule quantos dias de vida um fumante perderá. Exiba o total de dias

dia = int(input(f'Quantos cigarros fumados por dia: '))
anos = int(input(f'Quantos anos fumando: '))
total_C =((anos * 365) * dia)
total_m =(total_C * 10)
total_h =(total_m / 60)

print(f'O total de dias perdidos devido ao cigarro é: {total_h / 24: .1f} Dias')