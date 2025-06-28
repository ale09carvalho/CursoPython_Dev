
"""
# TODO - atividade 🐍💻: Crie um programa que faça as seguintes funções:
- Cadastre um novo usuário
- Liste todos os usuários cadastrados
- Alterar os dados de um usuário
- Fazer sorteio de usuário
- Exclua um usuário
- Saia do programa
# NOTE - dados do usuário:
- Nome completo
- Data de Nascimento
- E-mail
- CPF
- Telefone
- Gênero
- Data do cadastro (pegar do sistema)
- Hora do cadastro (pegar do sistema)
# NOTE - DIVIRTAM-SE!!! 💻😎👌
"""
#importando a biblioteca
import os
import datetime
from datetime import date

# formatando data e hora
data = date.today().strftime("%d/%m/%Y")
hora = datetime.datetime.now().strftime("%H:%M:%S")

lista = []

try:
    while True:
        usuario = {} #dicionario

        print(f"{'='*15} Menu {'='*15}")
        print("Informe a opao desejada:")
        print("1 - Cadastrar usuario:")
        print("2 - Alterar dados:")
        print("3 - Sortear Usuarios:")
        print("4 - Excluir  usuario:")
        print("0 - Sair:")

        opcao = input("Informe a Opçao desejada: ")

        match opcao:

            case "0":
                print("\nPrograma encerrado!\n")
                break
            case "1":                
                usuario['nome'] = input("Informe o nome:")  
                usuario['dataNascimento'] = input("Informe a data de nascimento (dd/mm/aa):")
                usuario['cpf'] = input("Informe o cpf:")
                usuario['email'] = input("Informe o e-mail:")
                usuario['telefone'] = input("Informe o telefone:")  
                usuario['genero'] = input("Informe o genero:")
                # data
                # hora
                lista.append(usuario)
                os.system("cls")
                print(f"{usuario.get('nome')} cadastrado com sucesso!\n")
                continue
            case "2":
                #os.system("cls")
                for i in range(len(lista)):
                    print(f"Posiçao: {i}: {nome}")

                posicao = int(input("Informe a posição do usuario que deseja alterar: "))
                
                if lista[posicao]:
                    for chave in lista[posicao]:
                        print(f"{chave.title()}: {lista[posicao].get(chave)}")
                        print("\n")
                        dado = input("Informe o nome da chave que deseja alterar: ")
                        if lista[posicao][dado]:
                            lista[posicao][dado] = input(f"Informe o novo valor de {dado}: ")
                            os.system("cls")
                            print("Dados alterado com sucesso!\n")
                        else:
                            print("Chave invalida!")
                    else:
                        print("Posiçao invalida!")
                        continue
            case "3":
                posicao = random.randint(0, len(nome)-1) # random.randint(0, len()-1) busca um número aleatório entre 0 e o tamanho da lista - 1
                print(f"Nome sorteado: {nome[i]}")
                continue
            case "4":
                os.system("cls")
                posicao = int(input("Informe a posição do usuario que deseja deletar: "))
                if lista[posicao]:
                    del(lista[posicao])
                    print("Usuario deletado com sucesso!")
                else:
                     print("Não foi possivel deletar o usuario!")
                continue
            case _:
                print("Opçao invalida!")
                continue

except Exception as e:
    print(f"Nao foi possivel executar a operaço. {e}.")
    
