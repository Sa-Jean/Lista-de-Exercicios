#Ex 4 - Questão D. Daniela é uma pessoa muito supersticiosa. Para ela, um número é sortudo
# se ele contém o dígito 2 mas não o dígito 7. Então, na opinião dela, quantos números
# sortudos existem entre 18644 e 33087, incluindo os extremos?
# Resposta: 7995

lista = [*range(18644, 33088, 1)]
tem2 = []
for numero in lista:
    if '2' in str(numero) and '7' not in str(numero):
        tem2.append(numero)

print(len(tem2))