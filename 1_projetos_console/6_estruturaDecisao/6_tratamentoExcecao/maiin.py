# tratamento de exceção
# try...except é uma estrutura de decisão usada para tratamento de exceções. 
try:
    n = int(input("Digite um número inteiro: "))
    print(f"O número que você informou é: {n}")

except Exception as e:
    print(f"Nao foi possivel exibir o numero. {e}. ")
    
# O bloco finally é executado independentemente de uma exceção ter sido levantada ou não.
finally:
    print("Fim do programa. Obrigado por participar!")
