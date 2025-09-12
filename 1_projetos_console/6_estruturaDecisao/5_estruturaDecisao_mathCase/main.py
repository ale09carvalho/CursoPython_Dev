# declaraçao de variavel 
# entrada de dados
x = float(input('Informe o valor de X:').replace(',', '.'))
y = float(input('Informe o valor de Y:').replace(',', '.'))

# Estrutura de decisão com Math Case
# A estrutura match...case introduzida em versões recentes do Python
# igualdade de padrões, semelhante ao switch...case de outras linguagens.

# MENU 
print(f"\n{'-'*20} ESCOLHA A OPERAÇAO {'-'*20}\n")
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')

# Solicita ao usuário a escolha da operação
operador = input('Informe o número da operação: ').strip()
# .strip() é usado para remover espaços em branco no início e no final da string.

# match case 
match operador:
    case 1:
        #result = x + y
        #print(f'\nA soma de {x} + {y} é igual a {result}')

        print(f"A soma dos valores é {x + y}.")
    case 2:
        #result = x - y
        #print(f'\nA subtração de {x} - {y} é igual a {result}')

        print(f"A subtraçao dos valores é {x - y}.")
    case 3:
        # result = x * y
        # print(f'\nA multiplicação de {x} * {y} é igual a {result}')
        print(f"A multiplicação dos valores é {x * y}.")
    case 4:
        print(f" Divisão dos valores  é {x/y}")
    case _:
        print("Operação inválida. Por favor, escolha uma opção válida entre 1 e 4.")

# Fim do programa