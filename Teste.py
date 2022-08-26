data = input('dd / mm / aaa: ')
k = 0
troca = ''
while k < len(data):
    if data[k] in '/':
        troca = troca + 'de'
    else:
        troca = troca + data[k]
    k = k + 1


print([troca])
