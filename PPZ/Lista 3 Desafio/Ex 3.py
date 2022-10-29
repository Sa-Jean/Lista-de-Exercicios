#Ex 3 - Verifique se um inteiro positivo n é primo.

n = int(input('n: '))
k = 1
divisores = 0

while k <= n:
    if n % k == 0:
        divisores = divisores + 1
    k = k + 1
print(divisores == 2)