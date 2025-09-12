'''
Módulo os em Python é uma biblioteca padrão muito útil quando se trata de interagir com o sistema operacional.
fornece uma série de funcionalidades para executar ações específicas, 
como navegar por diretórios, criar novos diretórios, executar comandos no terminal e obter informações do sistema.
'''
# importar biblioteca
import os 

while True:
    nome = input("Informe seu nome: ")
    os.system("cls")
    print(f"Seja bem vindo, {nome}!")

    prosseguir = input("Deseja inserir outro nome? (s/n)").lower() .strip()

    match prosseguir:
        case "s":
            os.system("cls")
            continue
        case "n":
            break
        case _:
            print("Opçao invalida.")
            break