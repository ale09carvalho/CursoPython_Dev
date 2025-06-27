'''
Forma 3
É possível percorrer o dicionário como uma lista através de um laço de repetição, como o laço for, por exemplo:

'''

# dicionario
usuario = {
    'nome': "Alessandra",
    'idade': 40,
    'email': "ale09@gmail.com",
    'profissao': "programador"
}
#exibi os valores

for chave in usuario:
    # capitalize()método converte o primeiro caractere de uma string em uma letra maiúscula
    # string.capitalize()
    print(f"{chave.capitalize()}:{usuario.get(chave)}") 

    