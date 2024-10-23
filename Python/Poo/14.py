"""Sistema Bancário - Abstração, Encapsulamento:
Crie um sistema bancário que inclua classes para representar Conta Corrente e Conta Poupança. Utilize 
abstração para definir métodos como sacar, depositar e mostrar_saldo. Encapsule os atributos 
sensíveis, como saldo.
"""

class Conta:
    def __init__(self, numero):
        self.__numero = numero

    def sacar(self, sacar):
        pass

    def depositar(self, depositar):
        pass

    def mostrar_saldo(self):
        pass
    
class ContaCorrente(Conta):
    def __init__(self, numero):
        super().__init__(numero)
        self.__saldo = 0.0

    def sacar(self, sacar):
        if self.__saldo < 0:
            print("Saldo insuficiente na conta corrente")
        else:
            self.__saldo -= sacar
            print(f"Sacado com sucesso o valor de {sacar} R$ na conta corrente.")

    def depositar(self, depositar):
        self.__saldo += depositar
        print(f"Saldo depositado com sucesso na conta corrente: {depositar} R$")

    def mostrar_saldo(self):
        print(f"O saldo na conta corrente é de {self.__saldo} R$")

class ContaPoupanca(Conta):
    def __init__(self, numero):
        super().__init__(numero)
        self.__saldo = 0.0

    def sacar(self, sacar):
        if self.__saldo < 0:
            print("Saldo insuficiente na conta poupança")
        else:
            self.__saldo -= sacar
            print(f"Sacado com sucesso o valor de {sacar} R$ na conta poupança.")

    def depositar(self, depositar):
        self.__saldo += depositar
        print(f"Saldo depositado com sucesso na poupança: {depositar} R$")

    def mostrar_saldo(self):
        print(f"O saldo na poupança é de {self.__saldo} R$")


# Conta Corrente
print("\nCONTA CORRENTE")

conta_corrente = int(input("Digite o numero da conta corrente: "))
corrente = ContaCorrente(conta_corrente)
corrente.mostrar_saldo()

depositarCorrente = float(input("\nDigite o valor a ser depositado na conta corrente: "))
corrente.depositar(depositarCorrente)
corrente.mostrar_saldo()

sacarCorrente = float(input("\nDigite o valor a ser sacado na conta corrente: "))
corrente.sacar(sacarCorrente)
corrente.mostrar_saldo()

# Conta Poupança
print("\nCONTA POUPANÇA")

conta_poupanca = int(input("Digite o numero da conta poupança: "))
poupanca = ContaPoupanca(conta_poupanca)
poupanca.mostrar_saldo()

depositarPoupanca = float(input("\nDigite o valor a ser depositado na conta poupança: "))
poupanca.depositar(depositarPoupanca)
poupanca.mostrar_saldo()

sacarPoupanca = float(input("\nDigite o valor a ser sacado na conta poupança: "))
poupanca.sacar(sacarPoupanca)
poupanca.mostrar_saldo()