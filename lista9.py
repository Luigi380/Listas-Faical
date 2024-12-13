"""
1)
frase = input("Digite uma frase: ").lower()
contA = frase.count('a')
contE = frase.count('e')
contI = frase.count('i')
contO = frase.count('o')
contU = frase.count('u')

dicionarioVogais = {
                    'A' : contA, 
                    'E' : contE, 
                    'I' : contI, 
                    'O' : contO, 
                    'U' : contU
                    }
print(dicionarioVogais)
"""

"""
2)
lista_compras = {}

while True:
    nome_produto = input("Digite o nome do produto (ou 'FIM' para sair): ")
    
    if nome_produto.upper() == "FIM":
        break
    
    preco_produto = input(f"Digite o preço de {nome_produto}: ")
    
    if preco_produto.replace('.', '', 1).isdigit() and preco_produto.count('.') <= 1:
        preco_produto = float(preco_produto)
        lista_compras[nome_produto] = preco_produto
    else:
        print("Preço inválido! Por favor, insira um valor numérico válido.")

print("\nLISTA DE COMPRAS:")
for produto, preco in lista_compras.items():
    print(f"{produto}: R${preco:.2f}")

produto_excluir = input("\nDigite o nome do produto a ser excluído (ou 'não' para não excluir nada): ")

if produto_excluir in lista_compras:
    del lista_compras[produto_excluir]
    print(f"\nProduto '{produto_excluir}' excluído com sucesso!")
else:
    print("\nProduto não encontrado na lista.")

print("\nLISTA DE COMPRAS ATUALIZADA:")
for produto, preco in lista_compras.items():
    print(f"{produto}: R${preco:.2f}")
"""

"""
3)
notas_alunos = {}
medias_alunos = {}

while True:
    nome_aluno = input("Digite o nome do aluno (ou 'fim' para encerrar): ")
    
    if nome_aluno.lower() == "fim":
        break
    
    while True:
        try:
            nota1 = float(input(f"Digite a primeira nota de {nome_aluno}: "))
            if 0 <= nota1 <= 10:
                break
            else:
                print("Nota inválida! A nota deve ser entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Digite um número entre 0 e 10.")
    
    while True:
        try:
            nota2 = float(input(f"Digite a segunda nota de {nome_aluno}: "))
            if 0 <= nota2 <= 10:
                break
            else:
                print("Nota inválida! A nota deve ser entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Digite um número entre 0 e 10.")
    
    notas_alunos[nome_aluno] = [nota1, nota2]
    
    media = (nota1 + nota2) / 2
    medias_alunos[nome_aluno] = media

reprovados = 0
recuperacao = 0
aprovados = 0

print("\nResultado final dos alunos:")
for aluno, media in medias_alunos.items():
    if media < 5:
        reprovados += 1
        status = "Reprovado"
    elif media < 7:
        recuperacao += 1
        status = "Recuperação"
    else:
        aprovados += 1
        status = "Aprovado"
    
    print(f"{aluno}: Média = {media:.2f} - {status}")

print("\nResumo:")
print(f"Alunos Reprovados: {reprovados}")
print(f"Alunos de Recuperação: {recuperacao}")
print(f"Alunos Aprovados: {aprovados}")
"""