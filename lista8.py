"""
1)
meu_dicionario = {
    "chave1": "valor1",
    "chave2": 42,
    "chave3": [1, 2, 3],
    "chave4": {"Luigi": "Legal"},
    "chave5": "valor5",
    "chave6": 3.14
}

print("Valores do dicionário:")
for valor in meu_dicionario.values():
    print(valor)

print("\nChaves do dicionário:")
for chave in meu_dicionario.keys():
    print(chave)

print("\nChaves e valores do dicionário:")
for chave, valor in meu_dicionario.items():
    print(f"{chave}: {valor}")
"""

"""
2)
estoque = { 'tomate': [1000, 2.59],
            'alface': [500, 0.99],
            'batata': [2000, 1.89] }

print("---------MENU---------")
print("1) Tomate")
print("2) Alface")
print("3) Batata")
print("4) Visualizar itens na lista")
print("0) Sair do MENU")
opcao = input("Escolha uma opção:")

listaVenda = []
while opcao != "0":
    if opcao == "1":
        qtdProduto = int(input("Qual quantidade deseja levar: "))
        listaVenda.append(["tomate", qtdProduto])
    elif opcao == "2":
        qtdProduto = int(input("Qual quantidade deseja levar: "))
        listaVenda.append(["alface", qtdProduto])
    elif opcao == "3":
        qtdProduto = int(input("Qual quantidade deseja levar: "))
        listaVenda.append(["batata", qtdProduto])
    elif opcao == "4":
        print("Os itens listados abaixo estão no Menu:")
        print(listaVenda)
    else:
        print("Valor selecionado é inválido")

    # exibir o menu novamente.
    print("---------MENU---------")
    print("1) Tomate")
    print("2) Alface")
    print("3) Batata")
    print("4) Visualizar itens na lista")
    print("0) Sair do MENU")
    opcao = input("Escolha uma opção:")

venda = listaVenda
total = 0
print("Vendas: \n")

for operacao in venda:
    produto, quantidade = operacao
    preco = estoque[produto][1]
    custo = preco * quantidade
    print("%12s : %3d x %3.2f = %6.2f \n" % (produto, quantidade, preco, custo))
    estoque[produto][0] = estoque[produto][0] - quantidade
    total += custo
print("Custo total : %3.2f \n" % total)
print("Estoque: \n")

for chave, dados in estoque.items():
    print("Descrição:", chave)
    print("Quantidade:", dados[0])
    print("Preço: %3.2f \n" % dados[1])
"""

"""
3)
frase = input("Escreva uma frase (evite colocar caracteres especiais): ").lower()
totalCaracteres = {}
for caractere in frase:
    if caractere != " " and caractere != ",":
        if caractere in totalCaracteres:
            totalCaracteres[caractere] += 1
        else:
            totalCaracteres[caractere] = 1
print(totalCaracteres)
"""