'''
# TODO - Atividade : Crie um programa que  receba do usuario, o nome, o peso em Kg e a altura em metros, e calcule o valor do IMC (Indice de Massa Corporal).
 o programa deve mostrar o nome do usuario, o IMC arrendondado para  2 casa decimais, e mostrar o diagnostio do usuario com base nos seguintes valores:
 - Caso o IMC seja menor que 18.5 = abaixo do peso
 - Caso o IMC seja maior ou igual 18.5 e menor que 25 = peso ideal
 - Caso o IMC seja maior ou igual 25 e menor que 30 = acima do peso.
 - Caso o IMC seja maior ou igual 30 e menor que 35 = obeso
 - Caso o IMC seja maior ou igual 35 e menor que 40 = obesidade nivel 2.
 - Casp o IMC seja maior ou igual a 40 = Obsesidadde mórbida.

 # NOTE - o usuario devera informar o encerrmamento do programa, ou seja, ele poderá repetir o calculo quantas vezes desejar.
'''
while True:
    try:
        # entrada de dnados
        nome = input("Informe seu nome: "). title() .strip()
        peso = float(input("Informe o seu peso em Kg: ").replace(',', '.'))
        altura = float(input("Informe a sua altura em metros: ").replace(',', '.'))
        imc = peso / altura **2
        
        print(f"O valor do IMC de {nome} é {imc:.2f}. ")

        # Verifica se os valores são positivos antes de calcular o IMC
        if imc < 18.5:
            print(f"{nome} - Voce esta abaixo do peso")
        elif imc < 25:
            print(f"{nome} -  Voce esta no peso ideal")
        elif imc < 30 :
            print(f"{nome} - Voce esta acima do peso")
        elif imc < 35:
            print(f"{nome}  - Voce esta com obeso")    
        elif imc < 40:
            print(f"{nome}  - Voce esta com obesidade nivel 2 ")
        else:
            print(f"{nome}  - Voce esta com obesidade mórbida")
        
        while True:
        # Pergunta se o usuário deseja continuar
            prosseguir = input("Deseja realizar outro cálculo? (s/n): ").strip().lower()
            if prosseguir == "s" or prosseguir == "n":
                break
            else:
                print("Opção inválida.")
                continue
        match prosseguir:
             case 's':
                  continue
             case 'n':
                  print("Programa encerrado.")
                  break
             case _:
                  print("Opção inválida. Programa encerrado.")
                  continue
    # Tratamento de exceções
    except Exception as e:
            print(f"Erro ao calcular o IMC: {e}. Por favor, tente novamente.")
            continue
    # Fim do programa