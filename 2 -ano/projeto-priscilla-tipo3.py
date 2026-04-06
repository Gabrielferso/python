class ContaBancaria:
    def __init__(self, saldo, numero, tipo_conta):
        self.saldo = saldo
        self.numero = numero
        self.tipo_conta = tipo_conta

    def getSaldo(self):
        return self.saldo
    def getNumero(self):
        return self.numero
    def getTipoConta(self):
        return self.tipo_conta

    def setSaldo(self, saldo):
        self.saldo = saldo

    def setNumero(self, numero):
        self.numero = numero

    def setTipoConta(self, tipo_conta):
        self.tipo_conta = tipo_conta
    
    def verificar_situacao(self):
        if self.saldo > 0:
            print(f"O saldo da conta {self.numero} está positivo.")
        elif self.saldo < 0:
            print(f"O saldo da conta {self.numero} está negativo.")
        else:
            print(f"A conta {self.numero} está sem saldo.")

def main():
    saldo = float(input("Digite o saldo da conta: "))
    numero = int(input("Digite o número da conta: "))
    tipo_conta = input("Digite o tipo da conta: ")

    conta = ContaBancaria(saldo, numero, tipo_conta)
    conta.setSaldo(saldo)
    conta.verificar_situacao()
    print(f"O saldo atual da conta número {conta.getNumero()} é: {conta.getSaldo()}")

main()