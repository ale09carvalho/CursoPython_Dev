#bibliotecas 
import os
import random

# Lista
nomes = [] # lista vazia

while True:
    print(f"{'='*10}MENU{'='*20}\n")
    print("Escolha a opção.")
    print(" [1] - Inserir nome na lista.")
    print(" [2] - Exibir lista.")
    print(" [3] - Sortear nome.")
    print(" [4] - Sair do programa.")

    opcao = input("Digite a opção: ").strip()
    os.system("cls" if os.name == "nt" else "clear")

    match opcao:
        
        case "1": # Inserir nome na lista
            try:
                novo_nome = input("Informe o nome: ").strip().title()
                os.system("cls" if os.name == "nt" else "clear")
                nomes.append(novo_nome) # adiciona o nome na lista
                print("Nome inserido com sucesso!")

            except Exception as e:
                print(f"Erro ao inserir nome na lista: {e}")
            finally:
                continue           
             
        case "2": # Exibir lista
            try:
                 nomes.sort() # ordena a lista
                 for nome in nomes: # percorre a lista
                    print(nome)
                    print("-" * 30)
            except Exception as e:
                print(f"Erro ao exibir a lista: {e}")
            finally:
                continue
        case "3": # Sortear nome
            i = random.randint(0, len(nomes)-1) # random.randint(0, len()-1) busca um número aleatório entre 0 e o tamanho da lista - 1
            print(f"Nome sorteado: {nomes[i]}")
            continue

        case "4": # Sair do programa
            print("Saindo do programa...")
            break

        case _: # Opção inválida
            print("Opção inválida. Tente novamente.")
            continue
        