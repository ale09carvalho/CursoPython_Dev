# Lista
# inserir um novo item na lista
nomes = [
    "Alex",
    "Joana",
    "Mariana",
    "Mario",
    "Ferananda"
]

# exibe a lista
for nome in nomes:
    print(nome)

# o usuareio informa o nome a ser acrescenta na lista
novo_nome = input("Infomre o novo nome a ser acrescentado: ").title().strip() # title() deixa a primeira letra maiúscula e o resto minúscula, strip() remove espaços extras

# novo nome é insarido na lista
nomes.append(novo_nome) # append() adiciona o novo nome ao final da lista

# exibe a lista atualizada
for nome in nomes:
    print(f"Olá, {nome}!")

# fim