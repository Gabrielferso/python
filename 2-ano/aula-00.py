class carro:
    def __init__ (self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        print("Em andamento...  ")

    def descrevrer(self):
        return f"{self.marca} {self.modelo}, Cor: {self.cor}"
    
meu_carro = carro("Toyota", "Corolla", "Prata")
carrinho = carro("Hot wheels", "Ford Ka", "Azul com rosa")

print(meu_carro.descrevrer())
print(meu_carro.marca)

print(carrinho.descrevrer())