#Ex 5 - Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando o algoritmo de Euclides

def main():

    n = int(input("Digite n: "))
    m = int(input("Digite m: "))

    anterior  = n
    atual     = m

    resto = atual % anterior
    while resto != 0:
        resto = anterior % atual;
        anterior = atual;
        atual = resto;

    print("MDC(%d,%d)=%d" %(n,m,anterior))

#-------------------------------------------------
main()