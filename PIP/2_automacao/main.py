#Automaçao
import pyautogui as auto
import time

def main():
    auto.PAUSE = 1
    auto.press("win")  #abre o menu iniciar
    auto.write("bloco de notas") # abrir a aplicaçao word
    auto.press('enter') # aperta enter após a digitação do nome do programa
    auto.press('enter')
    time.sleep(2)
    auto.hotkey("ctrl", "t")
    time.sleep(2)
    auto.write("linguagem de programação")
    

if __name__ == "__main__":
    main()

