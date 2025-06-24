'''
# lista - equivalente ao vetor - consiste em um conjunto de dados de um mesmo tipo armazenado 
em uma UNICA VARIAVEL

'''
nomes = ["Fulano", "Cicrano", "Beltrano", "João", "Maria", "José"]

# ordena a lista
# método da lista sort()classifica os elementos de uma lista
# list.sort(reverse=True)ordenará em ordem reversa
nomes.sort(reverse=True)

# imprime a lista na tela
for nome in nomes:
    print(nome)
# fim