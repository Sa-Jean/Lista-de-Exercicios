#Ex 2 - Determine se um ano é bissexto.Verifique no Google como fazer isso

ano = int(input('Ano: '))
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print('Bissexto')
else:
    print('Não é bissexto')