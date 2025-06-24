'''
# TODO - ATIVIDADE : Criar um programa que mostre a hora atual sempre quando atualizada a casa segundo
# NOTE - para  interroper o programa, use a tecla de atalho Ctrl + C
'''
import datetime
from datetime import datetime
import time
import os

print("Pressuione Ctrl + C a qualquer momento para interroper o programa.")
print("--------")

try:
    while True:
        # Limpar o terminal antes de imprimir a nova hora.
        # 'cls' p/ Windows e 'clear' p/ sistemas Unix (Linux/macOs)
        os.system("cls" if os.name == "nt" else "clear")
        
        horaAtual = datetime.now().strftime("%H:%M:%S")
        print(f"Hora atual: {horaAtual}")
        time.sleep(1) # Espera 1 segundo antes de atualizar novamente
except KeyboardInterrupt:
    print("\n Programa interropido pelo usuario")
except Exception as e:
    print(f"Ocorreu um erro : {e}")