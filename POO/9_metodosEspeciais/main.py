import Pessoa

def main():
    usuario = Pessoa.Pessoa(nome="ALE", idade=17)

    print(usuario)
    print(f"Idade: {len(usuario)}")

    # destruiçao do objeto
    del(usuario)
    #print(usuario)# dara um erro pois o objeto foi destruido

if __name__ == "__main__":
    main()