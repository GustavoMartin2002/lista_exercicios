"""28.Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe 
deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os 
métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, 
com valor default zero e os demais atributos são obrigatórios."""

class ContaCorrente:
    def __init__(self, numeroConta, nomeCorrentista):
        self.numeroConta = numeroConta
        self.nomeCorrentista = nomeCorrentista
        self.saldo = 0.0
    
    def alterarNome(self, setNome):
        self.nomeCorrentista = setNome
        print(f"Nome alterado com sucesso! Novo nome = {self.nomeCorrentista}")

    def deposito(self, valorDeposito):
        if valorDeposito <= 0:
            print("Insira um valor acima de 0 para ser depositado")
        else:
            self.saldo += valorDeposito
            print(f"Sucesso! O valor de {valorDeposito} foi depositado.")
    
    def saque(self, valorSaque):
        if self.saldo <= 0:
            print(f"Não é possivel sacar pois o saldo na sua conta é de {self.saldo}")
        else:
            self.saldo -= valorSaque
            print(f"Sucesso! O valor de {valorSaque} foi sacado.")
    
    def info(self):
        print(f"""
NUMERO DA CONTA:     {self.numeroConta}
NOME DO CORRENTISTA: {self.nomeCorrentista}
SALDO:               {self.saldo}  
        """)

numeroConta = int(input("Insira o numero da conta: "))
nomeCorrentista = input("Insira o nome do correntista: ")

conta = ContaCorrente(numeroConta,nomeCorrentista)

conta.info()
print("\n")

depositar = float(input("Insira o valor que deseja depositar na conta: "))
conta.deposito(depositar)

sacar = float(input("Insira o valor que deseja sacar da conta: "))
conta.saque(sacar)

setNome = input("Altere o nome do correntista: ")
conta.alterarNome(setNome)

print("\n")
conta.info()