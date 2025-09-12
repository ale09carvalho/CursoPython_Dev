#  While é um bloco que repete um algoritmo enquanto uma determinada condição for verdadeira.
# entrada de dados
n = int(input('Informe um número inteiro: '))

# Saída de dados
'''
Aqui entra em um loop infinito
while n < 0:
    print(n)
'''
#loop com condição de parada
while n >= 0:
    print (f"Número: {n}")
    # decrementa o valor de n
    # para que o loop não seja infinito
    n -= 1
  

