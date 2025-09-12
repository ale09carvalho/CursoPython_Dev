# Importaçoes
import os

# entrada de dados

while True:
    try:
        # usuario informa o nome do arquivo
        arquivo = input("Informe o nome do arquivo que deseja acessar: ").strip().lower()

        diretorio = input("Informe o diretorio do arquivo: ").strip()

        # abre o arquivo
        with open(f"{diretorio}/{arquivo}.txt", "r", encoding="utf-8") as f:
            arquivo_aberto = f.read()
        os.system("cls" if os.name == "nt" else "clear")

        #mostra os dados do arquivo
        print(arquivo_aberto)
        while True:
            prosseguir = input("Deseja abrir outro arquivo ? (s/n): ").strip().lower()
            if prosseguir == "s" or prosseguir == "n":
                break
            else:
                print("Opçao invalida.")
                continue
        match prosseguir:
            case "s":
                continue
            case "n":
                break
    except Exception as e:
        print(f"Nao foi possível ler o arquivo. {e}.")
        continue