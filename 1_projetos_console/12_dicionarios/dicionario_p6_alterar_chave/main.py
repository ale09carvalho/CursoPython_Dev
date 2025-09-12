# dicionario
usuario = {
    'nome': "Alessandra", 
    'idade': 45, 
    'email': "ale@gmail.com",
    'profissao': "programador"
    }
# exibi valores
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")
print("-"*40)

# Usuario informa a chave que deseja alterar
chave =input("Informe a chave que deseja alterar: ").lower().strip()

# usuario informa o valor da chave 
if chave in usuario:
    usuario[chave] = input(f"Infomre o novo valor de {chave}: ")
else:
    print("Chave inexistente.")

print("-"*40)
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")

