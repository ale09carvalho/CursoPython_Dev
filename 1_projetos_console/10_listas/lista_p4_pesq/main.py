# Lista

cidades = [
    "Brasília",
    "Goiânia",
    "Curitiba",
    "Florianópolis",
    "São Paulo",
    "Rio de Janeiro"
    "Brasília",
    "Teresina",
    "São Paulo",
    "Florianópolis",
    "Brasília"
]

# usuario informa o nome da ciadade a ser pesquisada 
cidade_pesquisada = input(("Infomre o nome da cidade : ")).title().strip() # title().strip() deixa a primeira letra maiúscula e o resto minúscula, remove espaços extras

# Programa conta quantas vezes ocorre o item pesquisado 
qtde = cidades.count(cidade_pesquisada) # count() - conta quantas vezes o item pesquisado ocorre na lista

# programa indica quantas vezes o item foi encontrado
print(f"{cidade_pesquisada} foi encontrada {qtde} vezes na lista.")