# LAMBDA - escrever funções de forma simplificada.
'''
Qdo funções são curtas apenas com o retorno, você pode trocar por um lambda,
que nada mais são do que funções sem nome, que já são atribuidas de forma direta às variáveis
'''
# Funçao Normal
# def somar(x,y):
#    result = x+ y
#    return result

# funçao com lambda
import os

somar = lambda x,y: x+y

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")


# Algoritmo principal
if __name__=="__main__":
    try:
        x = int(input("Informe o valor de x: "))
        y = int(input("Infomre o valor de y: "))
        limpar()
        result = somar(x,y)

        print (f"O resultado da soma é: {result}.")
    except Exception as e:
        print(f"Nao foi possivel somar os valores. {e}. '")