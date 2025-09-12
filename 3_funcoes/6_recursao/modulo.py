# função
# fatorial de um número natural, n!, é o produto de todos os números inteiros positivos menores ou iguais a n. 
# multiplicação do número por todos os seus antecessores até 1.

def fatorial(n):
    # n!
    return 1 if n == 0 else n * fatorial(n-1)