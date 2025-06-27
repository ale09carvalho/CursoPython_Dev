'''
Pode criar uma tupla com o nome das chaves desejadas. 
Assim,protege o dicionário contra alterações das chaves, caso precise, além de poder exibir os dados do dicionário em um laço for:

'''
# dicionario
usuario = dict(
    nome="Alessandra", 
    idde=40, 
    email="ale@gmail.com"
    )

# Forma 4
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")
    