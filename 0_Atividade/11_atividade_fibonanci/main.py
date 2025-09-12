"""
# TODO - atividade: crie um programa que receba do usuário um número inteiro e o programa calcula o valor da sequência de Fibonacci.

# A sequência de Fibonacci é uma série de números em que cada número é a soma dos dois números anteriores, 
# começando com 0 e 1
"""

# FUNÇAO RECURSIVA
def calcular_fibonacci(n):
    return n if n <= 1 else calcular_fibonacci(n-1) + calcular_fibonacci(n-2)

# ALGORITMO PRINCIPAL
# programa principal
n = int(input('Informe o número da sequências a ser calculada: '))
print(calcular_fibonacci(n))