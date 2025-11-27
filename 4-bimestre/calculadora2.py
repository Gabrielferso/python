while True:
    ent_a, opr, ent_b = input().split()
    ent_a = int(ent_a)
    ent_b = int(ent_b)
    
    def calcular(a, b, operacao):
        if operacao == "+":
            resultado = a + b
            return resultado
        elif operacao == "-":
            resultado = a - b
            return resultado
        elif operacao == "*":
            resultado = a * b
            return resultado
        elif operacao == "/":
            resultado = a / b
            return resultado
    

    x = calcular(a=ent_a, b=ent_b, operacao=opr)
    print(f"O resultado é igual a: {x}")