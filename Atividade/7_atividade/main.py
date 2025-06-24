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

lista = []

try:
    while True:
    # Menu
        print(f"{'='*10}MENU{'='*20}\n")
        print("Escolha a opção desejada.")
        print("1 - Cadastrar um novo nome na lista.")
        print("2 - Listar nomes cadastrados na lista.")
        print("3 - Pesquisar por um nome na lista.")
        print("4 - Alterar um nome na lista.")
        print("5 - Excluir um nome da lista.")
        print("6 - Sair do programa.")
    
    opcao = input("Informe a opção desejada: ").strip()
    
    match opcao:
        case "1":
            # Cadastrar novo nome na lista
            nome = input("Informe o nome a ser cadastrado: ").strip()
            lista.append(nome) # lista.append(nome) - Adiciona o nome à lista
            print(f"Nome '{nome}' cadastrado com sucesso!")

        case "2":
            # Listar nomes cadastrados na lista
            for i in range(len(nome)): # range(len()) - gera uma sequência de números de 0 até o tamanho da lista - 1
                print(f"Indice {i}: {nome[i]}")
        case "3":
            # Pesquisar por um nome na lista
            nome_pesquisada = input(("Infomre o nome para pesquisa: ")).title().strip()
            if nome_pesquisada in lista:
                print(f"Nome '{nome_pesquisada}' encontrado na lista.") 
            else:          
                print(f"Nome '{lista_pesquisada}' não encontrado na lista.")
        case "4":
            # TODO - Alterar um nome na lista
            ...
        case "5":
            # TODO - Excluir um nome da lista
            ...
        case "6":
            # TODO - Sair do programa
            ...
        case _:
            print("Opção inválida. Tente novamente.")
            continue

except Exception as e:
    print(f"Ocorreu um erro: {e}")
finally:
    print("Programa encerrado.")
    print(f"Lista final: {lista}")