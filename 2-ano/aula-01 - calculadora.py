class calculadora:
    def __init__ (self, cor, numero1, numero2):
        self.cor = cor
        self.numero1 = int(input("Digite o primeiro número: "))
        self.numero2 = int(input("Digite o segundo número: "))

    def somar(self):
        return self.numero1 + self.numero2
    
    def subtrair(self): 
        return self.numero1 - self.numero2
    
    def multiplicar(self):
        return self.numero1 * self.numero2
    
    def dividir(self):
        if self.numero2 != 0:
            return self.numero1 / self.numero2
        else:
            return "Erro: Divisão por zero não é permitida."
        
    def exibir_cor(self):
        return f"A cor da calculadora é: {self.cor}"
        
calc = calculadora("preta", 10, 5)
print(calc.somar())
print(calc.subtrair())
print(calc.multiplicar())
print(calc.dividir())
print(calc.exibir_cor())