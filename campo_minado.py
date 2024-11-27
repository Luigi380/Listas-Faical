import random

matriz = [["x " for _ in range(10)] for _ in range(10)]

def grade(matriz, tentativa_atual):
    
    j, i = tentativa_atual
    if (j, i) in posBomba:
        matriz[i][j] = "B "
    else:
        matriz[i][j] = f"{contBombas((j, i), posBomba)} "
  
    imprime_matriz(matriz)
 
def imprime_matriz(matriz):
    print("   A ", "B ", "C ", "D ", "E ", "F ", "G ", "H ", "I ", "J")

    for i, linha in enumerate(matriz):
        print(f"{i}  " + " ".join(linha))

def bomba(colunas, linhas):
    return [(random.randint(0, colunas - 1), random.randint(0, linhas - 1)) for _ in range(10)]

def eBomba(colunas, linhas, matriz):
    global posBomba
    posBomba = bomba(colunas, linhas)

    print("Posição da bomba (debug): ", posBomba)

    while True:
        escolhaLetra = input("Escolha uma coluna pela Letra correspondente: ").upper()
        if not (escolhaLetra.isalpha() and len(escolhaLetra) == 1):
            return print("Escolha uma letra válida!")
        
        escolhaNumero = escolhaNumero = int(input("Escolha uma linha pelo Número correspondente: "))
        
        # Converte a letra em um índice de coluna
        escolhaColuna = ord(escolhaLetra) - ord('A')

        tentativa_atual = escolhaColuna, escolhaNumero

        if tentativa_atual in posBomba:
            print("Você perdeu!")
            grade(revelarBombas(matriz, posBomba), tentativa_atual)
            break
        elif verifVitoria(colunas, linhas, tentativa_atual, posBomba):
            print("Parabéns! Você ganhou!")
            break
        else:
            grade(matriz, tentativa_atual)
            print("Continue!")

        marcador = input("Você quer marcar (S/N): ")
        if marcador.upper() == 'S':
            escolhaLetra = input(
                "Escolha uma coluna pela Letra correspondente: ").upper()
            if escolhaLetra.isalpha() and len(escolhaLetra) == 1:
                escolhaNumero = int(
                    input("Escolha uma linha pelo Número correspondente: "))

                escolhaColuna = ord(escolhaLetra) - ord('A')

                grade(marcar(escolhaColuna, escolhaNumero, matriz))
            else:
                return print("Escolha uma letra válida!")

def contBombas(jogada, coordenadas_bombas):
    linhas = colunas = 10
    x, y = jogada
    bombas_ao_redor = 0
    
    
    for i in range(max(0, x-1), min(linhas, x+2)):
        for j in range(max(0, y-1), min(colunas, y+2)):
            if (i, j) in coordenadas_bombas and (i, j) != jogada:
                bombas_ao_redor += 1

    return bombas_ao_redor

def marcar(coluna, linha, matriz):
    matriz[linha][coluna] = "M "
    return matriz

def verifVitoria(colunas, linhas, tentativas_feitas, posBombas):
    total_posicoes = colunas * linhas
    posicoes_sem_bombas = total_posicoes - len(posBombas)

    if len(tentativas_feitas) == posicoes_sem_bombas:
        return True
    return False

def revelarBombas(matriz, posBomba):
    for (j, i) in posBomba:
        matriz[i][j] = "B "
    return matriz

colunas = 10
linhas = 10
imprime_matriz(matriz)
eBomba(colunas, linhas, matriz)