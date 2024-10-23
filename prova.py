"""
1)
posição = 0
largura_total = 20
meio = largura_total // 2
while True :
    posicao_atual = meio + (posição//10)
    linha = ""
    for i in range(largura_total):
        if i == posicao_atual :
            linha += "|>"
        else :
            linha += "="
        print(linha)
        deslocamento = int(input('informe o deslocamento(negativo para azul e positivo para vermelho):'))
        posição += deslocamento
    if posição <= -100:
        print("azul vencedor ")
        break
    elif posição >= 100 :
        print("vermelho vencedor ") 
        break
"""

"""
2)
figura = input("Escolha a figura (losango ou triangulo): ")
tamanho = int(input("Digite o tamanho (número de linhas): "))
if figura == 'losango':
    for i in range(tamanho):
        print(' ' * (tamanho - i - 1) + '%' * (2 * i + 1))
    for i in range(tamanho - 2, -1, -1):
        print(' ' * (tamanho - i - 1) + '%' * (2 * i + 1))
elif figura == 'triangulo':
    for i in range(tamanho):
        print('%' * (i + 1))
else:
    print("Escolha inválida. Por favor, digite 'losango' ou 'triangulo'.")
"""