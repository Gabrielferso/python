def dividir_comando(linha):
    partes = [p.strip() for p in linha.split(",")]
    if partes[0] == "":
        return "", []
    acao = partes[0]
    args = partes[1:]
    return acao, args

def registrar_historico(historico, contador, resultado):
    historico[contador] = {"resultado": resultado}

def cadastrar_servidor(servidores, nome, matricula):
    if matricula in servidores:
        return "Servidor já cadastrado."
    servidores[matricula] = {"nome": nome, "matricula": matricula}
    return f"{nome}, matrícula {matricula}, cadastrado com sucesso."

def listar_servidores(servidores, chaves):
    if len(servidores) == 0:
        return "Ainda não há servidores cadastrados."
    linhas = []
    for mat, dados in servidores.items():
        chave_atual = None
        for cod, info in chaves.items():
            if info["servidor"] == mat and info["status"] == "indisponível":
                chave_atual = cod
                break
        if chave_atual is not None:
            linhas.append(f"{mat} — {dados['nome']} — com a chave {chave_atual}")
        else:
            linhas.append(f"{mat} — {dados['nome']} — sem chave")
    return "\n".join(linhas)

def adicionar_chave(chaves, codigo, descricao):
    if codigo in chaves:
        return "Chave já registrada."
    chaves[codigo] = {"descrição": descricao, "status": "disponível", "servidor": None}
    return f"Chave {codigo} cadastrada com sucesso."

def alterar_chave(chaves, codigo, nova_desc):
    if codigo not in chaves:
        return "Chave não encontrada."
    chaves[codigo]["descrição"] = nova_desc
    return f"Descrição da chave {codigo} atualizada para {nova_desc}."

def retirar_chave(chaves, servidores, codigo, matricula):
    if codigo not in chaves:
        return "Chave não encontrada."
    if matricula not in servidores:
        return "Servidor não encontrado."
    for cod, info in chaves.items():
        if info["servidor"] == matricula and info["status"] == "indisponível":
            return "Servidor já possui uma chave."
    if chaves[codigo]["status"] == "indisponível":
        return "Chave já está indisponível."
    chaves[codigo]["status"] = "indisponível"
    chaves[codigo]["servidor"] = matricula
    nome = servidores[matricula]["nome"]
    return f"Chave {codigo} retirada por {nome} (matrícula {matricula})."

def devolver_chave(chaves, servidores, codigo, matricula):
    if codigo not in chaves:
        return "Chave não encontrada."
    if matricula not in servidores:
        return "Servidor não encontrado."
    if chaves[codigo]["status"] == "disponível":
        return "A chave já está disponível."
    chaves[codigo]["status"] = "disponível"
    chaves[codigo]["servidor"] = None
    nome = servidores[matricula]["nome"]
    return f"Chave {codigo} devolvida por {nome} (matrícula {matricula})."

def listar_chaves(chaves, servidores):
    if len(chaves) == 0:
        return "Nenhuma chave encontrada."
    linhas = []
    for codigo, dados in chaves.items():
        linha = f"{codigo} — {dados['descrição']} — {dados['status']}"
        if dados["servidor"] is not None:
            mat = dados["servidor"]
            nome = servidores[mat]["nome"]
            linha += f" — responsável: {nome} ({mat})"
        linhas.append(linha)
    return "\n".join(linhas)

def ver_status(chaves, servidores, codigo):
    if codigo not in chaves:
        return "Chave não encontrada."
    dados = chaves[codigo]
    texto = f"Código: {codigo}\nDescrição: {dados['descrição']}\nStatus: {dados['status']}"
    if dados["status"] == "indisponível":
        mat = dados["servidor"]
        texto += f"\nServidor responsável: {servidores[mat]['nome']} ({mat})"
    return texto

def historico_geral(historico):
    if len(historico) == 0:
        return "Nenhum registro no histórico."
    linhas = []
    for num, dados in historico.items():
        linhas.append(f"{num} - {dados['resultado']}")
    return "\n".join(linhas)

def historico_servidor(chaves, servidores, matricula):
    if matricula not in servidores:
        return "Servidor não encontrado."
    registros = []
    for cod, dados in chaves.items():
        if dados["servidor"] == matricula:
            registros.append(f"Chave {cod} — {dados['descrição']}")
    if len(registros) == 0:
        return "O servidor não possui registro de retirada de chaves."
    return "\n".join(registros)

def processar_comando(acao, args, servidores, chaves, historico):
    if acao == "cadastrar_servidor":
        return cadastrar_servidor(servidores, args[0], args[1])
    if acao == "listar_servidores":
        return listar_servidores(servidores, chaves)
    if acao == "adicionar_chave":
        return adicionar_chave(chaves, args[0], args[1])
    if acao == "alterar_chave":
        return alterar_chave(chaves, args[0], args[1])
    if acao == "retirar_chave":
        return retirar_chave(chaves, servidores, args[0], args[1])
    if acao == "devolver_chave":
        return devolver_chave(chaves, servidores, args[0], args[1])
    if acao == "listar_chaves":
        return listar_chaves(chaves, servidores)
    if acao == "ver_status":
        return ver_status(chaves, servidores, args[0])
    if acao == "historico_geral":
        return historico_geral(historico)
    if acao == "historico_servidor":
        return historico_servidor(chaves, servidores, args[0])
    if acao == "sair":
        return "FIM"
    return "Comando inválido."

def menu():
    print(f"=" * 30, " Menu de opções ", "=" * 30)
    print("| \033[91mCadastre um servidor:\033[0m cadastrar_servidor, nome, matrícula                  |\n" \
    "| \033[91mAdicione uma chave:\033[0m adicionar_chave, codigo, descrição                     |\n" \
    "| \033[91mModifique a chave:\033[0m alterar_chave, codigo, nova descrição                   |\n" \
    "| \033[91mRetire uma chave pelo servidor:\033[0m retirar_chave, codigo, matricula           |\n" \
    "| \033[91mDevolva a chave ao sistema:\033[0m devolver_chave, codigo, matricula              |\n" \
    "| \033[91mVeja os status das chaves:\033[0m ver_status                                      |\n" \
    "| \033[91mVeja a lista de todas as chaves:\033[0m listar_chaves                             |\n" \
    "| \033[91mVeja a lista de todos os servidores:\033[0m listar_servidores                     |\n" \
    "| \033[91mVeja todas as ações feitas por um servidor:\033[0m historico_servidor, matricula  |\n" \
    "| \033[91mVeja todas as ações feitas:\033[0m historico_geral                                |\n" \
    "| \033[91mSaia do sistema:\033[0m sair                                                      |")
    print("=" * 78)
    

def main():
    servidores = {}
    chaves = {}
    historico = {}
    contador = 0

    menu()

    while True:
        linha = input("Digite seu comando: ").strip().lower()
        if linha == "":
            continue
        acao, args = dividir_comando(linha)
        if acao == "":
            continue

        resultado = processar_comando(
            acao, args, servidores, chaves, historico
        )

        if resultado == "FIM":
            print("Sistema encerrado.")
            break

        print(resultado)

        if acao != "historico_geral":
            contador += 1
            registrar_historico(historico, contador, resultado)

main()