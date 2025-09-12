# Join - necessidade de juntar os valores de uma lista em uma única variável
# necessario ser string
dias_semana = [
    "Domingo",
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sabado"
]
# insere um separador (delimitador)
delimitador = " , "

# junta os nomes em uma única variável
dias_variavel = delimitador.join(dias_semana)

print(dias_variavel)