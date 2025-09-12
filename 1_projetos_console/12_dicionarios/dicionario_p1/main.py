'''
Dicionário um tipo de coleção similar às listas, a diferença para cada valor do dicionário, há uma chave associada àquele valor.
lista []
tupla ()
dicionario {}
lista = ['Fulano', 'Cicrano', 'Beltrano'] é uma lista.
tupla = ('Fulano', 'Cicrano', 'Beltrano') é uma tupla.
dicionario = {'nome':'Fulano', 'idade':40, 'profissao':'Programador'} 
'''
# dicionario
usuario = {
    'nome': "Alessandra",
    'idade': 40,
    'email': "ale09@gmail.com",
    'profissao': "programador"
}
# 1º Forma de exibir valores
print(usuario)

try:
    print(f"Nome: {usuario['nome']}")
    print(f"Idade: {usuario['idade']}")
    print(f"Profissão: {usuario['profissao']}")

except Exception as e:
    print(f"Nao foi possivel separa os valores. {e}.")

    
