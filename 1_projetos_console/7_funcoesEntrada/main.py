# declarando uma função para entrada de dados

# .title() é um método que converte a primeira letra de cada palavra em maiúscula e as demais em minúscula.
nome = input("Digite seu nome: ").title()
print(f"Seu nome é: {nome}")

# .capitalize() é um método que converte a primeira letra de uma string para maiúscula e as demais para minúscula.
texto = input("Digite uma frase: ").capitalize()
print(f"Frase: {texto}")

# .upper() é um método que converte todas as letras de uma string para maiúsculas.
minuscula = input("Digite um texto totalmento e caixa baixa (minúsculas)").upper()         
print(f"Texto em caixa alta(maiúscula): {minuscula}.")


# .lower() é um método que converte todas as letras de uma string para minúsculas.
maiuscula = input("Digite um texto totalmento e caixa alta (maiúsculas)").lower()
print(f"Texto em caixa baixa(minúscula): {maiuscula}.")

# str.strip() é um método que remove espaços em branco no início e no final de uma string.
texto_com_espacos = input("Digite um texto com espaços no início e no final: ").strip() 
print(f"Texto sem espaços: {texto_com_espacos}.")

# str.replace() é um método que substitui uma substring por outra em uma string.
texto_substituido = input("Digite um texto: ").replace("a", "e")  # Substitui 'a' por 'e'
print(f"Texto com 'a' substituído por 'e': {texto_substituido}.")