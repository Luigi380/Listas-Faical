"""
1)
multiplo = 7
soma = 0
for i in range(100,501):
    if i % multiplo == 0:
        soma = soma + i
print(f"A soma de todos os múltiplos de 7 entre 100 e 500 é {soma}")
"""

"""
2)
soma = 0
numeros10A50 = 0
for i in range(10):
    num = float(input("Informe o número:"))
    if 10 <= num <= 50:
        numeros10A50 += 1
    else:
        soma += num
print(f"Existem {numeros10A50} entre 10 e 50")
print(f"A soma dos números que não estão nesse intervalo é {soma}")
"""

"""
3)
for i in range(99,10,-2):
    print(i)
"""

"""
4)
cont = 0
for i in range(20):
    num = int(input("Insira o número:"))
    if num % 13 == 2:
        cont += 1

print(f"A quantidade de números que dão resto 2 é {cont}")
"""

"""
5)
numN = int(input("Digite um número:"))
numM = int(input("Digite um número:"))

if numN > numM:
    print("Ocorreu um erro! Inverta os números")
else:
    print("Os números pares entre os números N e M são:")
    for i in range(numN, numM, 2):
        if numN % 2 != 0:
            i += 1
        print(i)
"""

"""
6)
soma1 = 0
soma2 = 0
numN = int(input("Digite um número:"))
numM = int(input("Digite um número:"))

if numN > numM:
    print("Ocorreu um erro! Inverta os números")
elif numN < 0 or numM < 0:
    print("O números estão negativos. Escolha números positivos!")
else:
    for i in range(numN, numM + 1):
        if i % 3 != 0 and i % 7 != 0:
            soma1 += i
        elif i % 3 == 0 or i % 7 == 0:
            soma2 += i
print(f"A soma de todos os números do intervalo entre N e M que não são múltiplos de 3 nem de 7 é {soma1}")
print(f"A soma de todos os números do intervalo entre N e M que são múltiplos de 3 nem de 7 é {soma2}")
"""

"""
7)
numN = int(input("Insira um número do qual queira saber a tabuada:"))
for i in range(0, 11):
    multiplica = numN * i
    print(f"A multiplicação entre {numN} e {i} é igual a {multiplica}")
"""

"""
8)
soma = 0
for j in range(1, 51):
    for i in range(1, 100, 2):
        divisao = i / j
        soma += divisao
print(f"Soma dos resultados das divisões: {soma}")
"""

"""
9)
numN = int(input("Digite um número inteiro e positivo:"))
soma = 0
if numN < 0:
    print("Digite um número positivo!")
else:
    for i in range(1, numN + 1):
        divisao = 1 / i
        soma += divisao
print(f"A soma de todas as divisões é {soma}")
"""

"""
10)
numN = int(input("Insira um número que seja intero e positivo:"))
numM = int(input("Insira outro número que seja intero e positivo:"))
resultadoN = 1
resultadoM = 1
if numN < 0 or numM < 0:
    print("Os números tem que ser positivos!")
else:
    for i in range(1, numN + 1):
        resultadoN *= i
    for j in range(1, numM + 1):
        resultadoM *= j
    somaFatorial = resultadoN + resultadoM
    print(f"O fatorial de N é {resultadoN}")
    print(f"O fatorial de M é {resultadoM}")
    print(f"A soma desses fatoriais é {somaFatorial}")
"""

"""
11)
a = 1
b = 1
print(a)
print(b)
for i in range(1, 21):
    soma2Termos = a + b
    a = b
    b = soma2Termos
    soma =+ soma2Termos
    print(soma)
"""

"""
12)
jequitiba = 1.5
jaqueira = 1.1
jabuticabeira = 2.98

for i in range(1, 26):
    i /= 100
jequitiba += i
print(f"A Jequitibá vai ter {jequitiba} metros")

for j in range(1, 26):
    j *= 2
    j /= 100
jaqueira += j
print(f"A Jaqueira vai ter {jaqueira} metros")

print(f"A Jabuticabeira vai ter {jabuticabeira} metros")

if jequitiba > jaqueira and jequitiba > jabuticabeira:
    print("Depois de 25 anos a maior é a Jequitibá")
elif jaqueira > jequitiba and jaqueira > jabuticabeira:
    print("Depois de 25 anos a maior é a Jaqueira")
else:
    print("Depois de 25 anos a maior é a Jabuticabeira")
"""

"""
13)
qtdSexoM = 0
qtdSexoF = 0
nomeMenorAltura = ""
menorAltura = float('inf')
maiorAltura = 0
for i in range(1, 21):
    nome = input("Qual seu nome?")
    sexo = input("Qual sua sexualidade(M/F)?")
    altura = float(input("Qual sua altura?"))
    print("-----------------------------")

    if sexo.lower() == "m":
        qtdSexoM += 1
    elif sexo.lower() == "f":
        qtdSexoF += 1
    else:
        print("Selecione apenas M ou F!")
        break

    if altura > maiorAltura:
        maiorAltura = altura
    elif altura < menorAltura:
        menorAltura = altura
        nomeMenorAltura = nome
print(f"A maior altura é: {maiorAltura}")
print(f"Quantidade de pessoas do sexo feminino: {qtdSexoF}")
print(f"O nome da pessoa de menor altura é: {nomeMenorAltura}")
"""

"""
for i in range(32, 213):
    c = round(5 / 9 * (i - 32),1)
    print(f"{i}° em Fahrenheit é {c}° em Celsius")
"""