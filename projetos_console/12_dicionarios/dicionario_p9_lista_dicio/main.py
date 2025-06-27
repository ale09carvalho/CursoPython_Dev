
# lista de dicionários
usuarios = [
    {
        'nome':'Fulano',
        'idade':20,
        'profissao':'programador'
    },
    {
        'nome':'Cicrano',
        'idade':25,
        'profissao':'cientista'
    },
    {
        'nome':'Beltrano',
        'idade':30,
        'profissao':'gerente de projetos'
    }
]

# exibe os dados
for usuario in usuarios:
    print("-"*30)
    for chave in usuario:
        # chave.capitalize - primeira letra chave em maiúscula:
        print(f"{chave.capitalize()}: {usuario.get(chave)}")

