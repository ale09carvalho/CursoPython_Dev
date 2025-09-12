'''
# TODO - Atividade:
#  Crie um programa que RECEBA do usuario O VALOR do etanol e da gasolina em reais, e INFORME ao usuario qual e o melhor combustível para abastecimento.
# NOTE - o usuario poderá informar varias vezes os valores, e irá encerrar o programa quando desejar.
# NOTE Compensa o Etanol caso ele tenha até 70% do valor da gasolina.
'''

# entra de dados
try:   
    while True:
        gasolina = float(input('Informe o valor da gasolina: R$ ').replace(',', '.'))
        etanol = float(input('Informe o valor do etanol: R$ ').replace(',', '.'))

        # calcula se o etanol é 70% do valor da gasolina
        # utilizado o if else para verificar a condição
        if etanol <= (gasolina * 0.7):
            print('Atençao!! Sugiro que você abastecer com Etanol.')
        else:
            print('Atençao!! Sugiro que você abasteça com Gasolina!')

        # pergunta se deseja continuar
        continuar = input('Deseja informar novos valores? (s/n): ').strip().lower() # strip()/lower() remove espaços no início e no final, lower() converte para minúsculas
        if continuar != 's':
            break
except Exception as e:
    print(f'Ocorreu um erro: {e}')
finally:
    print('Programa encerrado!')
# Fim do programa