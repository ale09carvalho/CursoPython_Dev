import classes as c


def main():
    # instancia objeto da clsse Conta
    cc = c.ContaCorrente(
        titular="",
        cpf="", 
        agencia="1010-1", 
        conta="10101-1", 
        saldo=0.0)

    cc.consultar_dados()
    print(f"Saldo: R$ {cc.depositar(200)}")
    print(f"Saldo: R$ {cc.sacar(25)}")

    # TODO ...
    #---metodo set
    cc.nome = input("Informe o nome titular:").strip().title()
    cc.cpf = input("Informe o CPF:").strip().title()
    
    # chamando 
    print ("Dados")
    print(f"Nome titular: {cc.nome}")
    print(f"CPF: {cc.cpf}")
    print(f"Num agencia:{cc.agencia} ")
    print(f"Num conta: {cc.conta}")
    print(f"Saldo atual é {cc.saldo}")
    

if __name__ == "__main__":
    main()

