import json
import os

pessoa = {}

try:
    arquivo = input("Informe o arquivo: ").strip().lower()
    with open(f"FileManager/{arquivo}.json", "r", encoding="utf-8")as f:
        pessoas = json.load(f)

    # usuario informa os dados da nova pessoa
    pessoa['nome'] = input("Informe o nome: ").strip().title()
    pessoa['idade'] = int(input("Informe a idade: "))
    pessoa['cpf'] = input("Informe o CPF: ").strip()
    pessoa['rg'] = input("Informe o RG: ").strip()
    pessoa['data_nas'] = input("Informe a data nascimento: ").strip()
    pessoa['sexo'] = input("Informe o sexo: ").strip()
    pessoa['signo'] = input("Informe o signo: ").strip().capitalize()
    pessoa['mae'] = input("Informe nome da mae: ").strip().title()
    pessoa['pai'] = input("Informe o nome do pai: ").strip().title()
    pessoa['email'] = input("Informe o e-mail: ").strip().lower()
    pessoa['senha'] = input("Informe a senha: ")
    pessoa['cep'] = input("Informe o CEP: ").strip()
    pessoa['endereco'] = input("Informe o endereço: ").strip().title()
    pessoa['numero'] = int(input("Informe o numero : "))
    pessoa['bairro'] = input("Informe o bairro: ").strip().capitalize()
    pessoa['cidade'] = input("Informe a cidade: ").strip().title()
    pessoa['estado'] = input("Informe o estado: ").strip().upper()
    pessoa['telefone_fixo'] = input("Informe o telefone fixo: ").strip()
    pessoa['celular'] = input("Informe o numero celular com dd: ").strip()
    pessoa['altura'] = float(input("Informe a altura: ").replace(",","."))
    pessoa['peso'] = float(input("Informe o peso: ").replace(",","."))
    pessoa['tipo_sanguineo'] = input("Informe o tipo sanguineo: ").strip().capitalize()
    pessoa['cor'] = input("Informe a cor favorita: ").strip()

    # inserir o nome na lista
    pessoas.append(pessoa)

    # grava no arquivo json
    with open(f"FileManager/{arquivo}.json", "w", encoding="utf-8") as f:
        json.dump(pessoas,f,ensure_ascii=False, indent=4)
    
    # ler o arquivo json
    with open(f"FileManager/{arquivo}.json", "r", encoding="utf-8") as f:
        pessoas = json.load(f)

    print(f"{'-'*20} LISTA DE PESSOAS {'-'*20}")
    for pessoa in pessoas:
        for chave in pessoa:
            print(f"{chave.capitalize()}: {pessoa.get(chave)}")
        print('-'*40)

except Exception as e:
    print(f"Nao foi possivel inserir pessoa. {e}.")