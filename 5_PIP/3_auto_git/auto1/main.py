# TODO - atividade

'''
ctrl ; atalho para inserir comentário na linhas
Criar um programa para automatizar o commit e o push de um repositório para o GitHub.
Crie um programa automaçao: que comita o projeto de voces e envia o repositorio para o GitHub.

'''
import pyautogui as pag
import time

## define o tempo de espera para cada comando
pag.PAUSE = 0.5

# instruções
pag.press('win') # abre o menu iniciar
pag.write('code') # digita na barra de pesquisa do menu iniciar o nome do programa "chrome"
pag.press('enter') # aperta enter após a digitação do nome do programa


# instruções
time.sleep(2)
pag.hotkey('ctrl','j')
pag.write("cd '.\Aperfeicoamento em Python\CursoPython_Dev'")
pag.press('enter')
pag.write('git status')
pag.press('enter')
pag.write('git add .')
pag.press('enter')
pag.write('git status')
pag.press('enter')
pag.write('git commit -m "Repositorio atualizado por automacao."')
pag.press('enter')
pag.write('git push')
pag.press('enter')