
# dicionario
usuario = {
    'nome': "Alessandra",
    'idade': 40,
    'email': "ale09@gmail.com",
    'profissao': "programador"
}
# 2º Forma de exibir valores
    # função get()
    # caso a chave não exista, não irá retornar um erro, mas sim none, qualquer forma, o código será executado
    # {var.get('')}  | {var['']} -----> CPF: None

print(f"Nome: {usuario.get('nome')}")
print(f"Idade: {usuario.get('idade')}")
print(f"Profissão: {usuario.get('profissão')}")
print(f"CPF: {usuario.get('CPF')}")


    