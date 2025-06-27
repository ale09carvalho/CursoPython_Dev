# tupla das chaves
chaves = ("Nome", "Idade", "E-mail", "Telefone", "Profissão")

# dicionário
usuario = {
    chaves[0]: "Alessandra",
    chaves[1]: 45,
    chaves[2]: "ale09@gmail.com",
    chaves[3]: "(61) 9999-99-99",
    chaves[4]: "programador"
}

for chave in chaves:
    print(f"{chave}: {usuario.get(chave)}")
