import datetime
from datetime import date
import os

#os.system( "cls" if os.name == "nt" else "clear") 

hora = datetime.datetime.now().strftime("%H:%M:%S") #.strftime("%H:%M:%S") somente a hora
print(hora)

hoje = date.today().strftime("%d:%m:%Y") 
hora = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

print(f"Data da execuçao: {hoje}.")
print(f"Hora da execuçao: {hora}.")