# lista

nomes = [
    "Alex",
    "Fernanda",
    "Alexandre",
    "José",
    "Maria",
    "João",
    "Renata",
    "Ricardo",
    "Jason",
    "Marta"
]
# Exibe a lista 
# # percorrendo cada NOME da variável
for i in range(len(nomes)):  # range(len()) - gera uma sequência de números de 0 até o tamanho da lista - 1
    print(f"Indice {i}: {nomes[i]}")
# Tratamento de exceção
try:
    # O usuário informa o índice a ser removido
    i = int(input("Informe a posição do nome da lista: "))
    if i >= 0 and i < len(nomes):
        del (nomes[i])
        print("Nome excluido com sucesso!")
    else:
        print("Posiçao inválido!")
except Exception as e:
    print(f"Não foi possível realizar a operação: {e}")
finally:
    # Re-exibe a lista atualizada
    for i in range(len(nomes)):
        print(f"Indice {i}: {nomes[i]}")
