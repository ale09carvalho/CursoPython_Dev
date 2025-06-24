'''
TODO - Atividade 7 - Crei um program que faça as seguites operaçoes:
- Cadastre novo nome na lista
- Liste todos os nomes na lista
- Pequise por um nome na lista
- Altere um nome na lista
- Exclua um nome da lista
- Sair do programa
# NOTE - a lista deve começar vazia. Exemplo: lista = []

'''
# Lista

lista = []

while True:
    # Menu
    print(f"{'='*10}MENU{'='*20}\n")
    print("Escolha a opção.")
    print(" 1 - Cadastrar novo nome na lista.")
    print(" 2 - Listar todos os nomes na lista.")
    print(" 3 - Pesquisar por um nome na lista.")
    print(" 4 - Alterar um nome na lista.")
    print(" 5 - Excluir um nome da lista.")
    print(" 6 - Sair do programa")
    
    opcao = input("Informe a opção desejada: ").strip()
    
    match opcao:
        case "1":
            nome = input("Informe o nome a ser cadastrado: ").strip()
            lista.append(nome)
            print(f"Nome '{nome}' cadastrado com sucesso!")
        case "2":
            if not lista:
                print("A lista está vazia.")
            else:
                print("Nomes cadastrados:")
                for i, nome in enumerate(lista, start=1):
                    print(f"{i}. {nome}")
        case "3":
            nome = input("Informe o nome a ser pesquisado: ").strip()
            if nome in lista:
                print(f"Nome '{nome}' encontrado na lista.")
            else:
                print(f"Nome '{nome}' não encontrado na lista.")
        case "4":
            nome_antigo = input("Informe o nome a ser alterado: ").strip()
            if nome_antigo in lista:
                novo_nome = input("Informe o novo nome: ").strip()
                index = lista.index(nome_antigo)
                lista[index] = novo_nome
                print(f"Nome '{nome_antigo}' alterado para '{novo_nome}'.")
            else:
                print(f"Nome '{nome_antigo}' não encontrado na lista.")
        case "5":
            nome = input("Informe o nome a ser excluído: ").strip()
            if nome in lista:
                lista.remove(nome)
                print(f"Nome '{nome}' excluído da lista.")
            else:
                print(f"Nome '{nome}' não encontrado na lista.")
        case "6":
            print("Programa encerrado.")
            break
        case _:
            print("Opção inválida. Tente novamente.")