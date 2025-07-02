# criar e manipular arquivos.
# Leitura de arquivo r - encondig mapa de caracter tipo utf-8
with open("FileManager/texto.txt", "r", encoding="utf-8") as f:
    texto = f.read()

#saida de dados que estao dentro do arquivo texto.txt
print(texto)
