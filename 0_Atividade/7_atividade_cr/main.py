'''
TODO - Atividade 7 - Crei um program que faça as seguites operaçoes:
- Cadastre novo nome na lista
- Liste todos os nomes na lista
- Pequise por um nome na lista
- Altere um nome na lista
- Exclua um nome da lista
- Sair do programa
# NOTE - a lista deve começar vazia. Exemplo: lista = []
# tratameno de exceçao
'''
# Lista
import os

# Lista inicial vazia
nomes = []

# Laço repeticao
while True:
    # ----------------Menu------------------
    print(f"{'='*10}MENU{'='*20}\n")
    print("Escolha a opção desejada.")
    print(" [1] - Cadastrar um novo nome na lista.")
    print(" [2] - Listar nomes cadastrados na lista.")
    print(" [3] - Pesquisar por um nome na lista.")
    print(" [4] - Alterar um nome na lista.")
    print(" [5] - Excluir um nome da lista.")
    print(" [6] - Sair do programa.")
    
    opcao = input("Informe a opção desejada: ").strip()
    
    os.system("cls" if os.name == "nt" else "clear")  # Limpa o terminal
    
    match opcao:

        case "1":  # Cadastrar novo nome na lista
            try:
                novo_nome = input("Informe o nome a ser cadastrado: ").strip() .title()  # .title() - Converte a primeira letra de cada palavra para maiúscula
                nomes.append(novo_nome) # lista.append(nome) - Adiciona o nome à lista
                print(f"Novo nome {novo_nome} cadastrado com sucesso!")
            except Exception as e:
                print(f"Erro ao cadastrar o nome: {e}")
            finally:
                continue
        
        case "2": # Listar nomes cadastrados na lista
            try:
                for i in range(len(nomes)): # range(len()) - gera uma sequência de números de 0 até o tamanho da lista - 1
                    print(f"{i}: {nomes[i]}")
                print('-'*40)
            except Exception as e:
                print(f"Erro ao listar não foi possível exibir: {e}")
            finally:
                continue

        case "3": # Pesquisar por um nome na lista
            nome_pesquisado = input(("Infomre o nome para a pesquisa: ")).title().strip()
            os.system("cls" if os.name == "nt" else "clear")  # Limpa o terminal
            qtde = nomes.count(nome_pesquisado)  # nomes.count(nome) - Conta quantas vezes o nome aparece na lista
            print(f"{nome_pesquisado} aparece {qtde} vez(es) na lista.")
            continue

        case "4":  # TODO - Alterar um nome na lista
            try:
                i = int(input("Infome o indice a ser alterado: "))
                if i >= 0 and i < len(nomes):
                    nomes[i] = input("Informe o novo nome: ")
                    os.system("cls" if os.name == "nt" else "clear")  # Limpa o terminal
                    print("Nome alterado com sucesso!")
                else:
                    print("Posição inválida!")
            except Exception as e:
                print(f"Não foi possível alterar: {e}")
            finally:
                continue
        case "5":
            try:
                i = int(input("Informe a posição do nome a ser excluído: "))
                if i >= 0 and i < len(nomes): # len() - Retorna o tamanho da lista
                    del (nomes[i])  # del - Exclui o nome da lista
                    os.system("cls" if os.name == "nt" else "clear")  # Limpa o terminal
                    print("Nome excluído com sucesso!")
                else:
                    print("Posição inválida!")
            except Exception as e:
                print(f"Não foi possível realizar a operação: {e}")
            finally:
                continue
            ...
        case "6":
            print("Programa encerrado.")
            break
        case _:
            print("Opção inválida. Tente novamente.")
            continue
    # ----------------Fim do Menu------------------