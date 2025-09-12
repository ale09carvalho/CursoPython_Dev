# Lista

cidades = [
    "Brasilia",
    "São Paulo",
    "Rio de Janeiro",
    "Teresina",
    "Belo Horizonte",
    "Palmas"
]

 # exibe a lista e seus índices
for i in range(len(cidades)): # range(len()) - gera uma sequência de números de 0 até o tamanho da lista - 1
    print(f"Indice {i}: {cidades[i]}")

# tratamento de exceçao
try:
    # o usuário informa o nome da nova cidade a ser acrescentada na lista
    nova_cidade = input("Informe o nome da nova cidade: ").title().strip() # title().strip() deixa a primeira letra maiúscula e o resto minúscula, remove espaços extras
    i = int(input("Informe a posiçao da lista onde deseja inserir:"))

    if i >=0 and i < len(cidades):
        # insere novo item em uma posiçao na lista
        cidades.insert(i, nova_cidade)
        # exibe a lista atualizada
        print(f"Cidade inserida com sucesso! ")
    else:
        print("Indice inválido!")
except Exception as e:
    print(f"Não foi possivel inserir o item na lista: {e}")
finally:
    # re-exibe a lista atualizada
    for i in range(len(cidades)):
        print(f"Indice {i}: {cidades[i]}")


