class carro:
    def __init__ (self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor

    def descrevrer(self):
        return f"{self.marca} {self.modelo}, Cor: {self.cor}"
    
meu_carro = carro("Toyota", "Corolla", "Prata")

print(meu_carro.descrevrer())
print(meu_carro.marca)