""" Defina uma classe Funcionario com atributos de nome, salário e cargo, e um método para
calcular o aumento de salário de acordo com o cargo. Coordenador 3%, Gerente 5%, Presidente
8%."""

class Funcionario():
    def __init__(self, nome, salario,cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
    
    def calcular(self):
        if self.cargo == 'coordenador'.lower():
            taxa = 0.3
            self.salario += taxa * self.salario
        elif self.cargo == 'gerente'.lower():
            taxa = 0.5
            self.salario += taxa * self.salario
        elif self.cargo == 'presidente'.lower():
            taxa = 0.8
            self.salario += taxa * self.salario
        else:
            print("Cargo Invalido...")
        
        print(f"Nome: {self.nome}")
        print("Salario com aumento: ",self.salario)
        print(f"Taxa: {taxa:.2f}")

nome = input("Digite seu nome: ")
salario = float(input("Digite seu salario: "))
cargo = input("Digite seu cargo = (coordenador) || (gerente) || (presidente): \n")

pessoa = Funcionario(nome, salario, cargo)
pessoa.calcular()