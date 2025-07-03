import json
import os

try:
    # usuario informa o arquivo
    arquivo = input("Informe o arquivo: ").strip().lower()

    # Le json e desserializa para dicionario
    with open(f"FileManager/{arquivo}.json", "r", encoding="utf-8")as f:
        lista = json.load(f)

    # aplica as conversões
    for dado in lista:
        dado['altura'] = dado['altura'].replace(",",".")
        dado['altura'] = float(dado['altura'])
        dado['peso'] = float(dado['peso'])

    # serializa o dicionario em json e grava o arquivo
    with open (f"FileManager/{arquivo}.json", "w", encoding="utf-8")as f:
        json.dump(lista,f, ensure_ascii=False, indent=4)
    
    #Confirmação
    print("Conversão gravada com sucesso.")
except Exception as e:
    print(f"Nao foi possivel converter pessoa. {e}.")