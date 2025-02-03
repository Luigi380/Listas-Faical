produtos=[
    {
        "nome": "maquina de lavar",
        "valor": 1350.0,
        "quantidade": 12,
        "comentarios": ["bacana", "veio arranhada", "gasta muita energia"],
        "notas": [1, 1, 1, 3, 5, 1, 1, 2, 1, 1],
    },
    {
        "nome": "placa de video",
        "valor": 15732.99,
        "quantidade": 3,
        "comentarios": ["top", "tem raytracing", "muito rapida", "barulhenta", "esquenta bastante"],
        "notas": [5, 5, 5, 5, 5, 4, 5, 4, 4, 5, 5],
    },
    {
        "nome": "biografia - ozzy osbourne",
        "valor": 9.99,
        "quantidade": 30,
        "comentarios": ["bem maluco", "um monstro sagrado do rock"],
        "notas": [5, 1, 3, 4, 5, 5],
    },
    {
        "nome": "geladeira frost free",
        "valor": 2469.50,
        "quantidade": 4,
        "comentarios": ["gostei", "maior do que esperava", "linda", "nao produz gelo :O"],
        "notas": [4, 4, 5, 3, 3, 3, 4, 5, 1, 0],
    },
]

def numProdutos(produtos):
    return len(produtos)

def infos(produtos):
    informacoes = []
    for i in produtos:
        nome = i["nome"]
        numComentarios = len(i["comentarios"])
        notas = i["notas"]
        mediaNotas = round(sum(notas) / len(notas),2)
        informacoes.append({"nome": nome, "n° de comentários": numComentarios, "média de notas": mediaNotas})
    return informacoes

def ultimoComentario(produtos):
    comentarios = []
    for i in produtos:
        ultimoComen = i["comentarios"][-1]
        comentarios.append({"nome do produto": i["nome"], "útimo comentário": ultimoComen})
    return comentarios

def infosTerceiroProduto(produtos):
    terceiroProduto = produtos[2]
    return {"nome": terceiroProduto["nome"], "quantidade em estoque": terceiroProduto["quantidade"]}

def produtosAcimaDaMedia(produtos):
    notas = [nota for produto in produtos for nota in produto["notas"]]
    mediaGeral = sum(notas) / len(notas)
    acimaMedia = [
        produto["nome"]
        for produto in produtos
        if round(sum(produto["notas"]) / len(produto["notas"]),2) > mediaGeral
    ]
    return acimaMedia

def atualizaPreco(produtos):
    for i in produtos:
        i["valor"] = i["valor"] * 0.9
    return produtos

def vendaDoQuartoProduto(produtos):
    produtos[3]["quantidade"] -= 1
    return produtos

print(f"Número de produtos cadastrados: {numProdutos(produtos)}")

print("\nAs informações de cada produto:")
for i in infos(produtos):
    print(i)

print("\nÚltimos comentários:")
for i in ultimoComentario(produtos):
    print(i)

print(f"\nInformações do 3° produto: {infosTerceiroProduto(produtos)}")

print(f"\nProdutos que estão acima da média: {produtosAcimaDaMedia(produtos)}")

print("\nRedução do valor dos produtos em 10%:")
for i in atualizaPreco(produtos):
    print(i)

print("\nAtualização da lista de produtos após a venda do 4° produto")
for i in vendaDoQuartoProduto(produtos):
    print(i)