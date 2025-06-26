import os

# lista
nomes = [
    "Fulano",
    "Ciclano",
    "Beltrano",
    "Joao",
    "Maria",
    "Jose"
]
# extrair o nome e isolar em uma variável

#exibi a lista de nomes
for i in range(len(nomes)):
    print(f"{i} - {nomes[i]}")
    print("-" * 60)

try:
    i = int(input("Informe o indice que deseja separar:"))
    if i >= 0 and i < len(nomes):
        nome_isolado = nomes.pop(i) # remove o nome da lista e o armazena na variável nome_isolado

        os.system("cls" if os.name == "nt" else "clear")  # Limpa a tela do console

        print(f"{nome_isolado} separado com sucesso!")
    # exibe os valores sem o item isolado
    
    for i in range(len(nomes)):
        print(f"{i}: {nomes[i]}")
        print("-"*60)

    #exibe o item isolado
        print(f"Valor isolado da lista: {nome_isolado}.")
    else:
        print("Indice inválido!")    
except Exception as e:
    print(f"Não foi possivel executar a operaçao : {e}")
