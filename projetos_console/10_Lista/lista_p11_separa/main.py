todos_os_meses = "Janeiro, Fevereiro, Março, Abril, Maio, Junho, Julho, Agosto, Setembo, Outubro, Novembro, Dezembro"

# separando em uma lista
# A função split() faz contrário do join(), ou seja, pega os valores de uma variável e separa em elementos diferentes de uma lista:

# insere o separador para separar os valores e os insere em uma lista
meses = todos_os_meses.split(",")

# exibe a lista
for mes in meses:
    print(mes)