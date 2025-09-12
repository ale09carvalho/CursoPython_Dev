'''
Módulo fornece acesso à constantes e funções matemáticas comuns, incluindo aquelas definidas pelo padrão C.

'''

# importar biblioteca
import math as m

# exibi o numero do pi
print(f"Numero do pi: {m.pi}.")

# raiz quadrada
try:
    n = int(input("Informe um numero inteiro: "))
    print(f"A raiz quadrada de {n} é {m.sqrt(n)}.")

except Exception as e:
    
    print(f"Não foi possivel calcular a raiz quadrada. {e}.")


    


