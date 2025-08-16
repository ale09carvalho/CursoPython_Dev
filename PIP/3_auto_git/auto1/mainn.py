import pyautogui as p
import time

def limpar_credenciais():
    p.write("git config --global --unset user.name")
    p.press('enter')
    p.write("git config --global --unset user.email")
    p.press('enter')

if __name__ == "__main__": 
    # Define o tempo de espera para cada comando
    p.PAUSE = 0.5

    # Solicita ao usuário a mensagem do commit
    msg_commit = input("Informe a mensagem do commit: ")
       
   
    limpar_credenciais()  # Limpa as credenciais do git

    #p.write("cd '.\app_python\'") # Navega até o diretório do repositório
    p.write('git config --global user.name "ale09carvalho"') # Configura o nome de usuário
    p.press('enter')
    p.write('git config --global user.email "ale09.carvalho@gmail.com"') # Configura o e-mail
    p.press('enter')
    p.write('git status') # Verifica o status do repositório
    p.press('enter')
    p.write('git add .') # Adiciona todas as alterações
    p.press('enter')
    p.write('git status') # Verifica o status novamente
    p.press('enter')
    p.write(f'git commit -m "{msg_commit}"') # Realiza o commit com a mensagem fornecida
    p.press('enter')
    p.write('git push') # Envia as alterações para o repositório remoto
    p.press('enter')

    limpar_credenciais()  # Limpa as credenciais do git novamente