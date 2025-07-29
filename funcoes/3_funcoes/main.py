'''
main.py - refere-se geralmente ao arquivo principal de um projeto ou script
a convenção é usar o bloco if __name__ == "__main__"
para definir o ponto de entrada do código que será executado quando o script for rodado diretamente. 
__name__:
É uma variável especial em Python que indica o nome do módulo.

modulo.limpar_tela() #necessario indicar o arquivo modulo
'''

# importa modulo
import modulo as m

# algoritmo principal - bloqueia o import e manter a integridade do sistema
if __name__ == "__main__":
    
    while True:
        print(" 1 - Calcular area quadrado.")
        print(" 2 - Calcular area retângulo.")
        print(" 3 - Calcular area triângulo.")
        print(" 4 - Sair do programa.")

        opcao = input("informe a opçao desejada: ").strip()
        m.limpar_tela() #necessario indicar o arquivo modulo

        match opcao:
            case "1":
                try:
                    l = float(input("Informe o lado do quadrado: "))
                    a = m.area_quadrado(l)

                    print (f"Area do quadrado: {a}.")
                except Exception as e:
                    print( f"Erro. {e}.")
                finally:
                    continue
            case "2":
                try:
                    b = float(input(" Informe a base do retângulo: "))
                    h = float(input(" Informe a altura do retângulo: "))
                    a = m.area_retangulo(b,h)

                    print ( f"Area do retângulo: {a}.")
                except Exception as e:
                    print( f"Erro. {e}.")
                finally:
                    continue
            case "3":
                try:
                    b = float(input(" Informe a base do triângulo: "))
                    h = float(input(" Informe a altura do triângulo: "))
                    a = m.area_triangulo(b,h)

                    print (f" Area do triângulo: {a}.")
                except Exception as e:
                    print( f"Erro. {e}.")
                finally:
                    continue
            case "4":
                print(" Programa encerrado! ")
                break
            case _:
                print (" Opçao invalida. ")
                continue       
