# Gravar Arquivo
import os


while True:
    try:
        novo_texto = input(" Digite o texto:\n")
        nome_arquivo = input("Informe o nome do arquivo (SEM A EXTENSÃO)").strip().lower()
        with open(f"FileManager/{nome_arquivo}.txt", "w", encoding="utf-8") as f:
            f.write(novo_texto)
        os.system("cls" if os.name == "nt" else "clear")
        print(f"{nome_arquivo}.txt gravado com sucesso.")
        
        while True:
            prosseguir = input("Deseja gravar novo arquivo? (s/n):").strip().lower()
            if prosseguir == "s" or prosseguir == "n":
                break
            else:
                print("Opçao Inválida.")
                continue
            match prosseguir:
                case "s":
                    continue
                case "n":
                    break 
    except Exception as e:
        print(f"Nao foi possível gravar o arquivo. {e}.")
        continue