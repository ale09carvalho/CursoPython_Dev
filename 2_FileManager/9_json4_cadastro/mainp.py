import json
import os

usuarios = []
novo_arquivo = ""

while True:
    usuario = {}
  
    print(" [1] - Cadastrar novo usuário no JSON.")
    print(" [2] - Salver arquivo JSON.")
    print(" [3] - Realizar a leitura do JSON.")
    print(" [4] - Sair do programa.")
    opcao = input("Informe a opcao desejada: ")

    match opcao:
        case "1": # Cadastrar novo usuário
            usuario['nome'] = input("Informe o nome:").strip().title()
            usuario['idade'] = int(input("Informe a idade:"))
            usuario['email'] = input("Informe o e-mail:").strip().lower()

            usuarios.append(usuario)
            os.system("cls" if os.name == "nt" else "clear")

            print("Usuario cadastrado com sucesso. ")
            continue
        case "2": # Salvar arquivo JSON.
            novo_arquivo = input("Informe o nome do arquivo (SEM EXTENSÃO).").strip().lower()
            with open(f"FileManager/9_json4/{novo_arquivo}.json", "w", encoding="utf-8") as f:
                json.dump(usuarios, f, ensure_ascii=False, indent=4)

            os.system("cls" if os.name == "nt" else "clear")
            print("Arquivo salvo com sucesso.")
            continue

        case "3": # Realizar a leitura do JSON  alteraçao (if not -> novo_arquivo)
            if not novo_arquivo:
                novo_arquivo = input("Infomre o nome do arquivo: ").strip().lower()

            with open(f"FileManager/9_json4/{novo_arquivo}.json", "r", encoding="utf-8") as f:
                dados = json.load(f)

            print(f"{'-'*20} USUARIOS {'-'*20} ")
            for usuario in dados:
                for chave in usuario:
                    print(f"{chave.capitalize()}: {usuario.get(chave)}")
                print("-"*40)
            continue

        case "4": # Sair do programa
            print("Programa encerrado.")
            break
        case _:
            print("Opçao invalida ")
            continue
   