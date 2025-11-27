while True:
    entrada = input("acao,numero1,numero2: ").split(",")
    acao = entrada[0]
    numero_1 = entrada[1]
    numero_2 = entrada[2]

    if acao == "sair":
        print("encerrando calculadora")

    elif acao == "soma":
        def soma(numero_1 , numero_2):
            resultado = numero_1 + numero_2
            return resultado

        x = soma(numero_1, numero_2)
        print("o resultado da soma é igual a: ",x)

    elif acao == "subtração":
        def subtrair(numero_1 , numero_2):
            resultado = numero_1 - numero_2
            return resultado

        x = subtrair(numero_1, numero_2)
        print("o resultado da subtração é igual a: ",x)

    elif acao == "multiplicação":
        def multiplicar(numero_1 , numero_2):
            resultado = numero_1 * numero_2
            return resultado

        x = multiplicar(numero_1, numero_2)
        print("o resultado da multiplicação é igual a: ",x)

    elif acao == "divisão":
        def dividir(numero_1 , numero_2):
            resultado = numero_1 / numero_2
            return resultado

        x = dividir(numero_1, numero_2)
        print("o resultado da divisão é igual a: ",x)

    else:
        print("ação inválida")