1.1 Remover servidor

Só pode remover se ele não estiver com nenhuma chave.

def remover_servidor(servidores, chaves, matricula):
    if matricula not in servidores:
        return "Servidor não encontrado."
    for cod, info in chaves.items():
        if info["servidor"] == matricula:
            return "Servidor não pode ser removido, pois está com uma chave."
    del servidores[matricula]
    return f"Servidor {matricula} removido com sucesso."

1.2 Remover chave

Só pode remover se ela estiver disponível.

def remover_chave(chaves, codigo):
    if codigo not in chaves:
        return "Chave não encontrada."
    if chaves[codigo]["status"] == "indisponível":
        return "Chave não pode ser removida, pois está emprestada."
    del chaves[codigo]
    return f"Chave {codigo} removida com sucesso."

1.3 Pesquisar servidor por nome
def buscar_servidor_nome(servidores, nome):
    resultados = [
        f"{mat} — {dados['nome']}"
        for mat, dados in servidores.items()
        if nome.lower() in dados["nome"].lower()
    ]
    if not resultados:
        return "Nenhum servidor encontrado com esse nome."
    return "\n".join(resultados)

1.4 Pesquisar chave por descrição
def buscar_chave_desc(chaves, termo):
    resultados = [
        f"{cod} — {dados['descrição']}"
        for cod, dados in chaves.items()
        if termo.lower() in dados["descrição"].lower()
    ]
    if not resultados:
        return "Nenhuma chave encontrada com essa descrição."
    return "\n".join(resultados)
