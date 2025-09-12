'''
tuplas são um tipo de coleções muito similar às lista, funcionam da mesma maneira, e permitem algumas das mesmas operações.
A diferença é que os valores de uma tupla não podem ser modificadas, funcionam como um conjunto de constantes ao invés de variáveis.
As listas identificadas por colchetes [], enquanto as tuplas são identificadas pelos parênteses ().
lista []
tuplas ()
Começa com seus valores padrões, e terminam com esses mesmos valores, sem possibilidade de mudança.

'''

# tuplas
dias_da_semana = (
   "Domingo",
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sabado"
)
for dia in dias_da_semana:
    print(dia)

