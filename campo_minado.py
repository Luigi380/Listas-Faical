import random

tentativas_feitas = []

def grade(colunas, linhas):
    print("   A ", "B ", "C ", "D ", "E ", "F ", "G ", "H ", "I ", "J")
    for i in range(linhas):
        print(i, end=" ")
        for j in range(colunas):
            if (i, j) in tentativas_feitas:
                if (i, j) == posBomba:
                    print(" B ", end="")
                else:
                    print("   ", end="")
            else:
                print(" x ", end="")
        print()

def bomba(colunas, linhas):
    return random.randint(0, colunas - 1), random.randint(0, linhas - 1)

def eBomba():
    colunas = 10
    linhas = 10
    global posBomba
    posBomba = bomba(colunas, linhas)
    
    print("Posição da bomba (debug): ", posBomba)
    
    while True:
        escolhaLetra = input("Escolha uma coluna pela Letra correspondente: ").upper()
        escolhaNumero = int(input("Escolha uma linha pelo Número correspondente: "))

        # Converte a letra em um índice de coluna
        escolhaColuna = ord(escolhaLetra) - ord('A')
        tentativas_feitas.append((escolhaNumero, escolhaColuna))
        
        if (escolhaColuna, escolhaNumero) == posBomba:
            print("Você perdeu!")
            grade(colunas, linhas)
            break
            
        else:
            grade(colunas, linhas)
            print("Continue!")

colunas = 10
linhas = 10
grade(colunas, linhas)
eBomba()