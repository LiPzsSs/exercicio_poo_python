class ContaBancaria:
    def __init__(self, numero_conta, titular_conta, saldo = 0):
        self.numero_conta = numero_conta
        self.titular_conta = titular_conta
        self.saldo = saldo
    
    def depositar(self, deposito):
        if deposito > 0:
            self.saldo += deposito
            print(f"Deposito efetuado com sucesso! Novo saldo: R${self.saldo: .2f}")
        else:
            print(f"Deposito não efetuado! Saldo atual: R${self.saldo: .2f}")

    def sacar(self, saque):
        if self.saldo >= saque:
            self.saldo -= saque
            print(f"Saque efetuado com sucesso! Novo saldo: R${self.saldo: .2f}")
        else:
            print(f"Saque não ocorrido. Falta de saldo. Seu saldo atual é: R${self.saldo: .2f}")
    

conta = ContaBancaria(12345, "João da Silva")
print(f"Saldo inicial da conta de {conta.titular_conta}: R${conta.saldo: .2f}")

conta.depositar(1000)

conta.sacar(500)