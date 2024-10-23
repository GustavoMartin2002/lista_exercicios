"""19. Cadastro de Funcionários - Encapsulamento:
Crie uma classe Funcionario com atributos privados para nome, salário e cargo. Forneça métodos
públicos para acessar e modificar esses atributos de forma segura."""

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.__nome = nome
        self.__salario = salario
        self.__cargo = cargo

    def getNome(self):
        return self.__nome
    
    def getSalario(self):
        return self.__salario
    
    def getCargo(self):
        return self.__cargo

    def setTudo(self, nome, salario, cargo):
        self.__nome = nome
        self.__salario = salario if salario > 0 else self.__salario
        self.__cargo = cargo

    def exibir(self):
        print(f"""
        Nome:    {self.__nome}
        Cargo:   {self.__cargo}
        Salario: {self.__salario:.2f}
            """)
        
def menu():
    print("""
        1 - Exibir dados do funcionário
        2 - Alterar nome, salario e cargo
        3 - Sair
    """)
    return input("Escolha uma opção: ")

funcionario = Funcionario("Carlinhos", 4000, "Supervisor")

while True:
    opcao = menu()

    if opcao == '1':
        funcionario.exibir()

    elif opcao == '2':
        nome = input("Digite o novo nome: ")
        salario = float(input("Digite o novo salário: "))
        cargo = input("Digite o novo cargo: ")
        funcionario.setTudo(nome, salario, cargo)

    elif opcao == '3':
        print("Fechando...")
        break

    else:
        print("Opção invalida!!")