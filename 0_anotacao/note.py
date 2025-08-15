CONTEÚDO PROGRAM[ATICO: POO
conceitos fundamentais: Classes, objetos, herança e polimirfismo
encapsulamento e abstração
tratamento de exceções
_____________________________
 import classes as c

# função main para inserir cod pinc.
# metodo main
def main():
       # instaciar as classes
    usuario = c.PessoaFisica(nome="", cpf="", telefone="", endereco="")
    empresa = c.PessoaJuridica(nome_fantasia="", cnpj="", telefone="", endereco="")

    # definir os valores dos atributos - input usuario
    print("Entre com os dados do Usuário:\n")

    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.cpf =  input("Informe o cpf: ").strip()
    usuario.telefone =  input("Informe o telefone: ").strip()
    usuario.endereco =  input("Informe o endereço: ").strip().title()

# chama o metodo main
if __name__ == "__main__":
    main()

# Observaçao
todas as funçoes tem q ser criada antes do algoritmo principal
no python  exigem colacar as funçoes antes algoritmo principal
================================================
python -m venv .venv  
.venv\Scripts\activate
===============================================
-> deep_translator (instalar biblioteca externa)
pip install deep_translator
==============================================
AUTOMAÇAO (BIBLIOTECA EXTERNA)
pip install pyautogui
===========================================

