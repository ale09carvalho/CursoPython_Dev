# lista

itens = [
    "Chocolate",
    "Feijão",
    "Arroz",
    "Macarrão",
    "Biscoito",
    "Ovos",
    "Leite",
    "Frango"
    ]

# exibe a lista  de compras
for i in range(len(itens)): # range(len()) - gera uma sequência de números de 0 até o tamanho da lista - 1
    print(f"Indice {i}: {itens[i]}")


# o usuário informa o indice a ser alterado
# tratamento de exceção
try:
    i = int(input("Informe a posiçao do indice a ser alterado: "))

    if i >= 0 and i < len(itens):
        itens[i] = input("Informe o novo item: ").capitalize().strip() # capitalize() deixa a primeira letra maiúscula e o resto minúscula .strip() remove espaços extras
        print(f"Item alterado com sucesso!")
    else:
        print("Indice inválido!")

except Exception as e:
    print(f"Não foi possivel alterar o item na lista: {e}")
finally:
    for i in range(len(itens)):
        print(f"Indice {i}: {itens[i]}")


