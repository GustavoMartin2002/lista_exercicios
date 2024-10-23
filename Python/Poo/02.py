"""Defina uma classe ContaBancaria com atributos de saldo e número da conta, e métodos para
depositar e sacar dinheiro"""

class ContaBancaria:
    def __init__(self, conta):
        self.conta = conta
        self.saldo = 0

    def depositar(self, deposito):
        self.saldo += deposito
    
    def sacar(self, sacarConta):
        if self.saldo  <= 0:
            print(f"não é possivel sacar, saldo de {self.saldo}R$")
        else:
            self.saldo -= sacarConta
    
    def info(self):
        print(f"""
        Conta:   {self.conta}
        Saldo:   {self.saldo}
        """)

conta = int(input("digite o numero da conta: "))

pietro = ContaBancaria(conta)

deposito = float(input("Digite o saldo que deseja depositar: "))
ContaBancaria.depositar(pietro,deposito)
ContaBancaria.info(pietro)

sacarSaldo = float(input("Digite o quanto deseja sacar: "))
ContaBancaria.sacar(pietro, sacarSaldo)
ContaBancaria.info(pietro)

