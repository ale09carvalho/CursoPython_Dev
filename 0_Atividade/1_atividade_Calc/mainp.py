'''
# TODO - Atividade: --  PROFESSOR 
#  Crie um programa que RECEBA do usuario O VALOR do etanol e da gasolina em reais, e INFORME ao usuario qual e o melhor combustível para abastecimento.
# NOTE - o usuario poderá informar varias vezes os valores, e irá encerrar o programa quando desejar.
# NOTE Compensa o Etanol caso ele tenha até 70% do valor da gasolina.
'''
# Laço de repetiçao
while True: 
    # tratamento de exceçao
    try:
        # Entrada de dados
        etanol = float(input("Infome o valor do etanol: R$ ").replace(',','.'))
        gasolina = float(input("Infomre o valor da gasolina: R$ ").replace(',','.'))
        
        calculo = (etanol / gasolina)*100
        # verificaçao de valores
        
        # Resolver com Ternário 
        result = "gasolina" if calculo > 70 else "etanol"

        # Exibe o resultado
        print(f" O resultado = {calculo:.2f} %. Ou seja, Compensa abastecer com: {result} ") # :.2f formata o número para 2 casas decimais

        # pergunta se deseja continuar
        opcao = input( " Deseja refazer o cálculo? (s/n) " ).lower().strip()
        match opcao:
            case 's':
                continue
            case 'n':
                break
            case _:
                print("Opção inválida.")
                continue
    except Exception as e:
        print(f"Nao foi possível executar a operaçao: {e}")
        continue