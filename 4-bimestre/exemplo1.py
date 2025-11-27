def main():
    produtos = {}

    while True:
        linha = input().strip()
        if linha == "":
            continue

        acao, args = parse_command(linha)
        if acao == "":
            continue
    
        resultado = processar_comando(produtos, acao, args)

        if resultado == "FIM!":
            print("Programa encerrado.")
