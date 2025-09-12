# Na composição, obrigatoriamente um dos atributos de uma classe é um objeto de outra classe.
# há uma dependência de uma das classes em relação à outra.
import classes as c

def main():
     #instanciar
    proprietario = c.Pessoa(
        nome="", 
        cpf="", 
        email="", 
        telefone="",
        endereco=""
        )
    
    #instanciar
    carro = c.Veiculo(
        modelo="", fabricante="", cor="",
        placa="", ano="", proprietario=""
    )

    # inputs
    print("-----Dados do Proprietario:-----")
    proprietario.nome = input("Informe o nome:").strip().title()
    proprietario.cpf = input("Informe o CPF:").strip()
    proprietario.email = input("Informe o e-mail:").strip().lower()
    proprietario.telefone = input("Informe o Telefone:").strip()
    proprietario.endereco = input("Informe o Endereco:").strip().title()

    print("-----Dados do Veiculo:-----")
    carro.fabricante = input("Informe o fabricante:").strip().title()
    carro.modelo = input("Informe o modelo:").strip().title()
    carro.cor = input("Informe a cor do veiculo:").strip()
    carro.placa = input("Informe a Placa:").strip().upper()
    carro.ano = input("Informe o Ano do veiculo:").strip()

    #  atributo proprientario recebe objeto da classe Veiculo
    carro.proprietario = proprietario

    # Exibir dados
    print("---Exibindo Dados do Veículo:---\n")
    print(f"Fabricante: {carro.fabricante}")
    print(f"Modelo: {carro.modelo}")
    print(f"Cor do veículo: {carro.cor}")
    print(f"Placa do veiculo: {carro.placa}")
    print(f"Ano do veículo: {carro.ano}")
    print(f"Dados do proprientario do veículo:\n {carro.info_proprietario()}")

# evita o import
if __name__ == "__main__":
    main()