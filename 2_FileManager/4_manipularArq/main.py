# Abrir arquivo que ja existe e atualizar os dados do arquivo

try:
    nome_arquivo = input("Informe o nome do arquivo (SEM EXTENSAO): ").strip().lower()
    
    with open(f"FileManager/{nome_arquivo}.txt", "r", encoding="utf-8") as f:
        texto = f.read()
    print(texto)

    novo_texto = input("Digite o texto: \n")

    with open(f"FileManager/{nome_arquivo}.txt", "w", encoding="utf-8")as f:
    
        f.write(novo_texto)


except Exception as e:
    print(f"Nao foi possível atualizar o arquivo. {e}.")
