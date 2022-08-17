#Ex 4 - A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de formação é simples:
# os dois primeiros elementos são 1; a partir de então, cada elemento é a soma dos dois anteriores.
# Faça um algoritmo que leia um número inteiro calcule o seu número de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc

x = int(input('Digite um numero'))
def rec_fib(n):
    if n > 1:
        return rec_fib(n-1) + rec_fib(n-2)
    return n
for i in range(x):
    print(rec_fib(i))