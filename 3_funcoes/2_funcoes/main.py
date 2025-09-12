# Funçoes
# print e return desempenham papéis distintos
# return - pode armazenar em uma variavel - ideal e que utilize o return dentro das funçoes
'''
print exibe dados na saída padrão, geralmente o console, enquanto return encerra a execução de uma função e 
envia um valor de volta para quem a chamou.
print é usado para visualização, enquanto return é usado para obter resultados de funções. 

''' 

# funçao 
def mostrar_msg(nome):
    return f"Seja bem vindo, {nome}!"

# programa principal
nome = input("Informe o seu nome: ").strip().title()
print(mostrar_msg(nome))

