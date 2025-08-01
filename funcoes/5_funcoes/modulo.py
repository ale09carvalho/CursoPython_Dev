# Funções - returno so permiti retornar um valor -
'''
 return e yield usados para retornar valores de funções, mas com propósitos diferentes.
 return encerra a função e retorna um valor, enquanto yield é usado em funções geradoras para produzir uma sequência de valores;
'''
import math
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def primeiro_grau(a, b):
    # a*x +b = 0
    x = -b/a
    return x

def segundo_grau(a, b, c):
    # a*x2 + b*x + c = 0 --> a diferente de 0 
    # baskara delta = (b**2)-(4*a*c)
    # delta>0 (2 raizes reais) / delta = 0(não ha raizes reais)/delta < 0 (1 raiz)

    if a !=0:
        delta = (b**2)-(4*a*c)
        if delta > 0:
            # tenho 2 raizes reais 
            x1 = (-b+math.sqrt(delta)) / (2*a)
            x2 = (-b-math.sqrt(delta)) / (2*a)
            # yield -> retorna valor mas nao encerra a funçao
            yield f" x' = {x1}"
            yield f' x" = {x2}'
            
        elif delta == 0:
           yield " Não há raizes reais para x."
           ...
        else:
            x = -b/(2*a)
            yield f"x = {x}"
    else:
        yield primeiro_grau(b, c)