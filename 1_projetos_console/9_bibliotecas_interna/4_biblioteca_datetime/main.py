# O datetimemódulo fornece classes para manipulação de datas e horas.
from datetime import date

#data atual do sistema padrão internacional

hoje = date.today().strftime("%d/%m/%Y") # para converter o padrao nacional strftime("%d%m%Y") - strftime("%d%m%y") - OBS. y minusculo a data ano fica 2 ditos
print(hoje)

