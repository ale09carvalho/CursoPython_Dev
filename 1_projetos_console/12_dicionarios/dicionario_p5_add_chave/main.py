# dicionario
usuario = {
    'nome': "Alessandra", 
    'idade': 40, 
    'email': "ale@gmail.com"
    }

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")

# adcionado nova chave
usuario['profissão'] = input("Informe a profissão: ").strip()

print("-"*40)
for chave in usuario:
    print(f"{chave.capitalize()}:{usuario.get(chave)}")
    