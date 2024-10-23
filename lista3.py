"""
1)
morango = float(input("Quantos kg de morango você comprou?"))
if morango < 5:
    precoMorango = 22 * morango
elif morango >= 5:
    precoMorango = 20 * morango

maca = float(input("Quantos kg de maçã você comprou?"))
if maca < 5:
    precoMaca = 6 * maca
elif maca >= 5:
    precoMaca = 5 * maca

frutas = morango + maca

valorTotal = precoMorango + precoMaca
if frutas > 8 or valorTotal > 100:
    desconto = round(valorTotal * 0.1,2)
    print(f"Você comprou {frutas}kg de frutas por R${desconto}")
else:
    print(f"Você comprou {frutas}kg de frutas por R${valorTotal}")
"""

"""
2)
numero = int(input("Digite um número de 0 a 100:"))
numeroChave = int(input("Digite um número de 0 a 100 para ser seu número chave:"))

if numero > numeroChave:
    resposta = numero - numeroChave
    print(f"O seu número está a {resposta} números de distância do número chave")
else:
    resposta = numeroChave - numero
    print(f"O seu número está a {resposta} números de distância do número chave")
"""

"""
3)
idade = int(input("Digite uma idade de 1 a 3 anos:"))

if idade == 1:
    print("Peso provável Masculino: 8.5 Kg a 12.5 Kg")
    print("Peso provável Feminino: 7.5 Kg a 11.5 Kg")
elif idade == 2:
    print("Peso provável Masculino e Feminino: 10.1 Kg a 15.2 Kg")
elif idade == 3:
    print("Peso provável Masculino: 11.7 Kg a 18 Kg")
    print("Peso provável Feminino: 11.4 Kg a 17.95 Kg")
else:
    print("A idade deve ser de 1 a 3!")
"""

"""
4)
tc = float(input("Quanto tempo de contribuição você tem com o INSS?"))
id = int(input("Qual sua idade?"))
anoAposentar = int(input("Em que ano você pretende se aposentar?"))
anoAtual = int(input("Em que ano você está?"))
sexo = input("Qual seu sexo (M/F)?")

if anoAposentar > anoAtual or anoAposentar == anoAtual:
    if sexo.lower() == "f":
        aposentadoria = tc + id 
        tempoAposentar = ((anoAposentar - anoAtual) // 2) + 85
        if aposentadoria >= tempoAposentar:
            print("O empregado poderá se aposentar")
        else:
            print("O empregado não poderá se aposentar")
    elif sexo.lower() == "m":
        aposentadoria = tc + id
        tempoAposentar = ((anoAposentar - anoAtual) // 2) + 95
        if aposentadoria >= tempoAposentar:
            print("O empregado poderá se aposentar")
        else:
            print("O empregado não poderá se aposentar")
else:
    print("Ano inválido. Não é possível cálculo")
"""

"""
5)
caracter = input("Selecione um caracter (G – Geométrica; P – Ponderada; H – Harmônica; A – Aritmética):")

if caracter.lower() != "g" and caracter.lower() != "p" and caracter.lower() != "h" and caracter.lower() != "a":
    print("Erro. Caracter inválido!")
else:
    x = float(input("Digite um valor pra x:"))
    y = float(input("Digite um valor pra y:"))
    z = float(input("Digite um valor pra z:"))

    if caracter.lower() == "g":
        geometria = round((x * y * z) ** 1/3,2)
        print(f"O valor do calcúlo geométrico é {geometria}")
    elif caracter.lower() == "p":
        ponderada = round(((x + 2) * (y + 3) * z) / 6,2)
        print(f"O valor do calcúlo ponderado é {ponderada}")
    elif caracter.lower() == "h":
        harmonica = round( 1 / (1 / x) + (1 / y) + (1 / z),2)
        print(f"O valor do calcúlo harmonica é {harmonica}")
    elif caracter.lower() == "a":
        aritmetica = round((x + y + z) / 3,2)
        print(f"O valor do calcúlo aritmetica é {aritmetica}")
"""

"""
6)
horas = int(input("A quantas horas que o carro está estacionado (Coloque números inteiros!)?"))

if horas <= 2:
    preco = horas * 1
    print(f"Você vai pagar R${preco}")
elif horas >= 3 and horas <= 5:
    valor = horas - 2
    preco1 = 2 
    preco2 = round(valor * 1.4,2)
    vPago = preco1 + preco2
    print(f"Você vai pagar R${vPago}")
else:
    valor = horas - 5
    preco1 = 2
    preco2 = 3 * 1.4 
    preco3 = round(valor * 1.6,2)
    vPago = round(preco1 + preco2 + preco3,2)
    print(f"Você vai pagar R${vPago}")
"""

"""
7)
n1 = int(input("De um número inteiro (Evite repiti-los):"))
n2 = int(input("De um número inteiro (Evite repiti-los):"))
n3 = int(input("De um número inteiro (Evite repiti-los):"))

if n1 == n2 or n1 == n3 or n2 == n1 or n2 == n3:
    print("Evite colocar números iguais!")
else:
    if n1 > n2 and n1 > n3:
        if n2 > n3:
            soma = n1 + n2
            print(f"A soma dos dois números maiores é {soma}")
        else:
            soma = n1 + n3
            print(f"A soma dos dois números maiores é {soma}")
    elif n2 > n1 and n2 > n3:
        if n1 > n3:
            soma = n2 + n1
            print(f"A soma dos dois números maiores é {soma}")
        else:
            soma = n2 + n3
            print(f"A soma dos dois números maiores é {soma}")
    else:
        if n1 > n2:
            soma = n3 + n1
            print(f"A soma dos dois números maiores é {soma}")
        else:
            soma = n3 + n2
            print(f"A soma dos dois números maiores é {soma}")
"""

"""
8)
tipoCombustivel = input("Qual o seu tipo de combustível (A - Álcool; G - Gasolina)?")
qtdLitros = float(input("Quantos litros você comprou?"))
precoLitro = float(input("Qual o valor do Litro?"))

if tipoCombustivel.lower() == "a":
    if qtdLitros <= 20:
        valor = round(precoLitro * 0.03,2)
        print(f"Você vai pagar R${valor} pelo combustível")
    elif qtdLitros > 20:
        valor = round(precoLitro * 0.05,2)
        print(f"Você vai pagar R${valor} pelo combustível")
elif tipoCombustivel.lower() == "g":
    if qtdLitros <= 20:
        valor = round(precoLitro * 0.04,2)
        print(f"Você vai pagar R${valor} pelo combustível")
    elif qtdLitros > 20:
        valor = round(precoLitro * 0.06,2)
        print(f"Você vai pagar R${valor} pelo combustível")
else:
    print("Coloque um tipo correto de combustível!")
"""