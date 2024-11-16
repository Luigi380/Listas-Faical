"""
1)
def par(x):
    if x % 2 == 0:
        return True
    else:
        return False

numX = int(input("Digite um número x inteiro: "))
if par(numX) == True:
    print(f"O seu número {numX} é par")
elif par(numX) == False:
    print(f"O seu número {numX} é ímpar")
else:
    print("Erro!")
"""

"""
2)
def maiorNum(a, b):
    if a > b:
        return a
    else:
        return b

numA = float(input("Digite um número: "))
numB = float(input("Digite outro número: "))

if maiorNum(numA, numB) == numA:
    print(f"O maior número é: {numA}")
elif maiorNum(numA, numB) == numB:
    print(f"O maior número é: {numB}")
else:
    print("Erro!")
"""

"""
3)
def soma(a, b):
    soma1 = sum(range(a+1, b))
    return soma1

numA = int(input("Digite um número: "))
numB = int(input("Digite outro número: "))
resultado = soma(numA, numB)
print(f"O resultado da soma do intervalo dos números A e B é: {resultado}")
"""

"""
4)
def multiplica(x, y):
    return x * y

numX = int(input("Digite um número X: "))
numY = int(input("Digite um número Y: "))
print(f"A multiplicação desses números é: {multiplica(numX, numY)}")
"""

"""
6)
def potencia(x, y):
    return x ** y

numX = int(input("Digite um número X: "))
numY = int(input("Digite um número Y: "))
print(f"A potencia de X elevado a Y é: {potencia(numX, numY)}")
"""

"""
8)
def primo(numX):
    divisiveis = []
    
    for i in range(numX):
        if numX % (i + 1) == 0:
            divisiveis.append(i + 1)
    
    print(divisiveis)

    if divisiveis == [1, numX]:
        print("Este número é primo!")
    else: 
        print("Este número não é primo!")
    
numX = int(input("Digite um número inteiro: "))
primo(numX)
"""

"""
9)
def fat(n):
    if n < 0: 
        print("Digite números positivos!")
    elif n == 0 or n == 1:
        print(f"{n}! = 1")
    
    contador = 1
    for i in range(1, n + 1):
        contador *= i
    
    print(f"{n}! = {contador}")

numN = int(input("Digite um número inteiro: "))
fat(numN)
"""