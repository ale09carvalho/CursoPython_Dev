# tratamento de exceção
# a estrutura do try...except é a mesma do try...catch das outras linguagens de programação tradicionais.
# try...except é uma estrutura de decisão usada para tratamento de exceções. 
try:
    n = int(input("Digite um número inteiro: "))
    print(f"O número que você informou é: {n}")

except Exception as e:
    print(f"Nao foi possivel exibir o numero. {e}. ")