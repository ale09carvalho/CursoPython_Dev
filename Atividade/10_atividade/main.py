'''
# TODO - atividade: faça um CRUD (Create, Read, Update, Delete) em um JSON.

Opções do menu:
 - Criar novo arquivo JSON (usuario irá informa o diretório).
 - Abrir arquivo JSON (o usuário ira informar o diretorio).
 - Cadastrar novo usuario em um JSON.
 - Listar todos os usuarios de um arquivo JSON
 - Pesquisar por um usuario de um arquivo JSON
 - Alterar dados de um usuario em  um arquivo JSON.
 - Deletar usuario de um arquivo JSON
 - Sair do programa

 -- Dados do Usuario:--
 - Nome
 - Data de Nascimento
 - CPF
 - E-mail
 - Telefone
 - Filme Favorito
'''
import os
import json

usuarios = []

while True:
    usuario = {}
    print(" [1] - Criar novo arquivo JSON.")
    print(" [2] - Abrir arquivo JSON.")
    print(" [3] - Cadastrar novo usuario em um JSON.")
    print(" [4] - Listar todos os usuarios de um arquivo JSON.")
    print(" [5] - Pesquisar por um usuario de um arquivo JSON.")
    print(" [6] - Alterar dados de um usuario em  um arquivo JSON.")
    print(" [7] - Deletar usuario de um arquivo JSON.")
    print(" [8] - Sair do programa.")
    opcao = input("Informe a opcao desejada: ")

    match opcao:

        case "1": # Criar novo arquivo JSON
            novo_arquivo = input("Informe o nome do arquivo (SEM EXTENSÃO).").strip().lower()
            with open(f"Atividade/10_atividade/{novo_arquivo}.json", "w", encoding="utf-8") as f:
                json.dump(usuarios, f, ensure_ascii=False, indent=4)

            os.system("cls" if os.name == "nt" else "clear")
            print("Arquivo salvo com sucesso.")
            continue 

        case "2": # Abrir arquivo JSON
            try:
                nome_arquivo = input("Informe o nome do arquivo (SEM EXTENSAO): ").strip().lower()
                with open(f"Atividade/10_atividade/{nome_arquivo}.txt", "r", encoding="utf-8") as f:
                    texto = f.read()
                print(texto)
                novo_texto = input("Digite o texto: \n")
                with open(f"Atividade/10_atividade/{nome_arquivo}.txt", "w", encoding="utf-8")as f:
                    f.write(novo_texto)

            except Exception as e:
                    print(f"Nao foi possível abrir o arquivo. {e}.")

        case "3": # Cadastrar novo usuario em um JSON
            usuario['nome'] = input("Informe o nome:").strip().title()
            usuario['data_nasc'] = input("Informe a data de nascimento:")
            usuario['cpf'] = int(input("Informe o CPF:"))
            usuario['email'] = input("Informe o e-mail:").strip().lower()
            usuario['telefone'] = input("Informe a idade:").strip()
            usuario['filme_favorito'] = input("Informe o filme favorito:").strip()

            usuarios.append(usuario)
            os.system("cls" if os.name == "nt" else "clear")

            print("Usuario cadastrado com sucesso. ")
            continue
        case "4": # Listar todos os usuarios de um arquivo JSON
            ...
        case "5": # Pesquisar por um usuario de um arquivo JSON
            ... 
        case "6": # Alterar dados de um usuario em  um arquivo JSON
            ...
        case "7": # Deletar usuario de um arquivo JSON
            ...
        case "8": # Sair do programa
            print("Programa encerrado.")
            break
        case _:
            print("Opçao invalida ")
            continue
        
    



