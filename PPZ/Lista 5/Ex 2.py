#Ex 2 - Questão B. Quantas vezes o trecho de pseudocódigo seguinte imprime 'oi'? (obs: na nossa pseudo-
# linguagem, o laço inclui os extremos, ou seja, 1 até 4 significa 1, 2, 3, 4.)
# Para i = 1 até 9
#    i != 3, então
#       para j = 1 até 6
#          imprime 'oi'
# RESPOSTA: 48
a = []
for i in range(1, 10):
    if i != 3:
         for j in range(1, 7):
            a.append('oi')
            print('oi')

print(len(a))