'''
Modulo  import time - permite trabalhar com datas e horas e ela já vem instalada no Python, 
então basta fazer a importação dessa biblioteca para começar a usar.
'''
# importar biblioteca
import os 
import time

try:
    n = int(input("Informe um numero inteiro:"))

    while n >= 0:
        os.system("cls")
        print(f"{n}...")
        time.sleep(1)
        n -= 1

except Exception as e:
    print(f"Nao foi possivel executar a contagem. {e}.")
finally:
    os.system("cls")
    print("BOOOOMMMM!!!!!")