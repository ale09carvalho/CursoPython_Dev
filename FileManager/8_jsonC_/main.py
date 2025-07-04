# Modelo aluno Caleb - para analise codigo.
# cadastro de uma nova pessoa salvando no novo arquivo json
import json
pessoa = {}

nome_arquivo = input("Informe o nome do arquivo (sem extensão): ").strip().lower()
diretorio_arquivo = input("Informe o diretorio onde o arquivo está salvo: ").strip()

# lendo o arquivo json e dessarializa em um dicionario do python
with open(f"{diretorio_arquivo}{nome_arquivo}.json", "r", encoding="utf-8") as t:
    pessoas = json.load(t)

# obtendo as chaves do primeiro item da lista 'pessoas' para uso no cadastro de uma nova pessoa
lista_de_chaves = []    
for chave in pessoas[0].keys():
    lista_de_chaves.append(chave)
    
# transformando a lista em tupla
tupla_de_chaves = tuple(lista_de_chaves)
       
for chave in tupla_de_chaves:
    if chave in ('altura','peso'):
        pessoa[chave] = float(input(f"Informe o valor de '{chave.capitalize()}': ").strip().replace(",","."))
    elif chave in ('idade','numero'):
        pessoa[chave] = int(input(f"Informe o valor de '{chave.capitalize()}': ").strip())
    else:
        pessoa[chave] = input(f"Informe o valor de '{chave.capitalize()}': ")

# adiciona a nova pessoa na lista pessoas
pessoas.append(pessoa)
print(f"Pessoa '{pessoa.get('nome')}' cadastrada com sucesso!")

# gravando o cadastro da nova pessoa no arquivo json
with open(f"{diretorio_arquivo}{nome_arquivo}.json", "w", encoding="utf-8") as t:
    json.dump(pessoas, t, ensure_ascii=False, indent=4)

# lendo o arquivo json novamente apos gravacao da alteracao
with open(f"{diretorio_arquivo}{nome_arquivo}.json", "r", encoding="utf-8") as t:
    pessoas = json.load(t) # cria a lista de dicionarios em python

# saida dos dados
print(f"{'-'*20} LISTA DE PESSOAS {'-'*20}")
for pessoa in pessoas:
    for chave in pessoa:
        print(f"{chave.capitalize()}: {pessoa.get(chave)}")
    print('-'*40)