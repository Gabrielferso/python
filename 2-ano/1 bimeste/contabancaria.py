class ContaBancaria:  
    def __init__(self, saldo_inicial, titular):   
        self._saldo = saldo_inicial  
        self._titular = titular

    @property  
    def saldo(self):  
        return self._saldo 
    def depositar(self, valor):
        valor = float(input("Digite o valor a ser depositado: "))
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self._saldo:.2f}")
        else:
            print("Valor de depósito inválido. O valor deve ser positivo.")

    def sacar(self, valor):
        valor = float(input("Digite o valor a ser sacado: "))
        if valor > 0:
            if self._saldo >= valor:
                self._saldo -= valor
                print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self._saldo:.2f}")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("Valor de saque inválido. O valor deve ser positivo.")

conta = ContaBancaria(1000, "João")
print(f"Saldo inicial da conta de {conta._titular}: R${conta.saldo:.2f}")
conta.depositar(2000)
conta.sacar(2000)
conta.sacar(1500)