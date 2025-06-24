# Resolução professor
# Biblioteca
import os
import time
import datetime

# Exibe a hora atual

while True:
    hora = datetime.datetime.now()time.strftime("%H/%M/%S")
    os.system("cls" if os.name == "nt" else "clear")
    print(f"Hora atual:{hora}")
    time.sleep(1)
    