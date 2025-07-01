
"""
# TODO - atividade 🐍💻: Crie um programa que faça as seguintes funções:
- Cadastre um novo usuário
- Liste todos os usuários cadastrados
- Alterar os dados de um usuário
- Fazer sorteio de usuário
- Exclua um usuário
- Saia do programa
# NOTE - dados do usuário:
- Nome completo
- Data de Nascimento
- E-mail
- CPF
- Telefone
- Gênero
- Data do cadastro (pegar do sistema)
- Hora do cadastro (pegar do sistema)
# NOTE - DIVIRTAM-SE!!! 💻😎👌
"""
#importando a biblioteca
import os
import datetime
import random
from datetime import date

lista = []

# loop
while True:
    # dicionario
    usuario = {}

    print(f"{'='*20} Menu {'='*20}")
    print("Informe a opao desejada:")
    print(" [1] - Cadastrar novo usuario:")
    print(" [2] - Listar dados do usuario:")
    print(" [3] - Alterar dados:")
    print(" [4] - Sortear Usuarios:")
    print(" [5] - Excluir  usuario:")
    print(" [6] - Sair:")

    opcao = input("Informe a Opçao desejada: ").strip() # .strip retira espaço em branco
    # limpa a tela
    os.system("cls" if os.name == "nt" else "clear")

    match opcao:
        case "1":
            try:
                usuario['nome'] = input("Informe o nome:").strip().title()  
                usuario['dataNascimento'] = input("Informe a data de nascimento (dd/mm/aa):").strip()
                usuario['email'] = input("Informe o e-mail:").strip().lower() # .lower() caixa baixa
                usuario['cpf'] = input("Informe o cpf:").strip()
                usuario['telefone'] = input("Informe o telefone:").strip()
                usuario['genero'] = input("Informe o genero:").strip()
                usuario['data do cadastro'] = date.today().strftime("%d/%m/%Y")
                usuario['hora do cadastro'] = date.datetime.now().strftime("%H:%M:%S")

                lista.append(usuario)
                os.system("cls" if os.name == "nt" else "clear")
                
            except Exception as e:
                print(f"Nao foi possivel executar a operaço. {e}.")
            finally:
                continue

        case "2":
            try:
               for i in range(len(lista)):
                    print(f"Indice: {i}")

                    for chave in lista[i]:
                        print(f"{chave.capitalize()}: {lista[i].get(chave)}")
                    #print('-'*40)
            except Exception as e:
                print(f"Nao foi possivel executar a operaço. {e}.")
            finally:
                continue

        case "3":
            try:
                i = int(input("Informe o indice que deseja alterar:"))
                os.system("cls" if os.name == "nt" else "clear")
                if i >= 0 and i < len(lista):
                    print(f"{"-"*20} Dados do usuario:{"-"*20}")
                    for chave in lista[i]:
                        print(f"{chave.capitalize()}: {lista[i].get(chave)}")
                    print("\n")

                    while True:
                        chave_escolhida = input("Informe qual chave deseja alterar:").strip().lower()
                        if chave_escolhida in lista[i]:
                            lista[i][chave_escolhida] = input("Informe o novo valor de {chave_escolhida}: ")
                            os.system("cls" if os.name == "nt" else "clear")
                            print("Chave alterada com sucesso.")
                        else:
                            print("Chave inexistente.")

                        while True:
                            prosseguir = input("Deseja alterar outra chave? (s/n): ").strip().lower()
                            if prosseguir == "s" or prosseguir == "n":
                                break
                            else:
                                continue
                        match prosseguir:
                            case "s":
                                continue
                            case "n":
                                break
                else:
                    print("Indice invalido.")
            except Exception as e:
                print(f"Nao foi possivel executar a operaço. {e}.")
            finally:
                continue

        case "4":
            try:
                i = random.randint(0, len(lista)-1) # random.randint(0, len()-1) busca um número aleatório entre 0 e o tamanho da lista - 1
                print(f"Usuario sorteado.")
                for chave in lista[i]:
                    print(f"{chave.capitalize()}: {lista[i].get(chave)}")
            except Exception as e:
                print(f"Nao foi possivel executar a operaço. {e}.")
            finally:
                continue
        case "5":
            try:
                i = int(input("Informe a posição do usuario que deseja deletar: "))
                if i >= 0 and i < len(lista):
                    for chave in lista[i]:
                        print(f"{chave.capitalize()}: {lista[i].get(chave)}")
                    while True:
                        excluir = input("Tem Certeza? (s/n): ").strip().lower()
                        if excluir == "s" or excluir == "n":
                            break
                        else:
                            print("Opçao invalida.")
                            continue
                    match excluir:
                        case "s":
                            del(lista[i])
                            os.system("cls" if os.name == "nt" else "clear")
                            print(" Usuario excluido com sucesso.")
                        case "n":
                            os.system("cls" if os.name == "nt" else "clear")
                            print("Usuario nao exluido.")
                else:
                    print("Indice invalido.")
            except Exception as e:
                print(f"Nao foi possivel executar a operaço. {e}.")
            finally:
                continue
        case "6":
            print("\nPrograma encerrado!\n")
            break
        case _:
                print("Opçao invalida!")
                continue