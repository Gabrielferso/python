class Eletrodomestico :
    def __init__(self, ligado, voltagem, consumo):

        self.ligado = ligado
        self.voltagem = voltagem
        self.consumo = consumo

    def descrever(self):
        return f"{self.ligado} {self.voltagem} {self.consumo}"
    
    def setVoltagem(self): 
         self.voltagem = input("Digite a nova voltagem: ")
         return f"Voltagem atualizada para: {self.voltagem}"
    
    def getVoltagem(self):
        return f"A voltagem atual é: {self.voltagem}"
    
    def setConsumo(self):
        self.consumo = input("Digite o novo consumo: ")
        return f"Consumo atualizado para: {self.consumo}"
    
    def getVoltagem(self):
        return f"O consumo atual é: {self.consumo}"
    
    def isLigado(self):
        if self.ligado:
            return "O eletrodoméstico está ligado."
        else:
            return "O eletrodoméstico está desligado."
    
    def setligado(self, ligado):
        self.ligado = input("Digite '1' para ligar ou '2' para desligar: ")
        if self.ligado == '1':
            self.ligado = True
        elif self.ligado == '2':
            self.ligado = False
        else:
            return "Entrada inválida. Por favor, digite '1' para ligar ou '2' para desligar."
        return f"O estado do eletrodoméstico foi atualizado para: {self.ligado}"
    
tv1 = Eletrodomestico (True, 220, 100)
tv2 = Eletrodomestico (False, 110, 243)

print("A tv está ligada?", tv1.isLigado())
tv1.setligado(None)
tv1.setVoltagem()
tv1.setConsumo()
print(tv1.descrever())