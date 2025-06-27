# dicionario
usuario = {
    'nome': "Alessandra",
    'idade': 45,
    'email': "ale09@gmail.com",
    'profissao': "programador"
}

# exibi valores
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")
print("-"*40)

# usuario informa o valor da chave deseja excluir 
chave = input(f"Infome a chave que deseja excluir: ").lower().strip() # .lower().strip() maiúscula e sem espaços em branco

#Verifica se a chave existe 
if chave in usuario:
    # excluir chave
    del usuario[chave]
else:
    print("Chave inexistente.")

print("-"*40)
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")
