"""
1)
salario = float(input("Informe seu salario:"))
financiamento = float(input("Qual o valor do financeamento:"))
salFinanciamento = round(financiamento / salario,2)
if salFinanciamento <= 5:
    print("Financiamento Concedido")
else:
    print("Fianciamento Negado")
print("Obrigado por nos consultar")
"""

"""
2)
distanciaPerc1 = float(input("Qual foi a distância percorrida pelo 1° carro?"))
tempoPerc1 = float(input("Qual foi o tempo usado pelo 1° carro?"))

distanciaPerc2 = float(input("Qual foi a distância percorrida pelo 2° carro?"))
tempoPerc2 = float(input("Qual foi o tempo usado pelo 2° carro?"))

velocidadeMed1 = round(distanciaPerc1 / tempoPerc1,2)
velocidadeMed2 = round(distanciaPerc2 / tempoPerc2,2)
if velocidadeMed1 > velocidadeMed2:
    print("O 1° carro foi o mais rápido")
elif velocidadeMed1 == velocidadeMed2:
    print("Os dois alcançaram velocidades iguais")
else:
    print("O 2° carro foi o mais rápido")
"""

"""
3)
nome1 = input("Qual seu nome?")
idade1 = int(input("Qual sua idade?"))

nome2 = input("Qual seu nome?")
idade2 = int(input("Qual sua idade?"))

anoAtual = int(input("Em que ano você está?"))
anoNasc1 = anoAtual - idade1
anoNasc2 = anoAtual - idade2

if idade1 > idade2:
    print(f"A pessoa mais nova é {nome2}")
    print(f"{nome2} nasceu no ano {anoNasc2}")
else:
    print(f"A pessoa mais nova é {nome1}")
    print(f"{nome1} nasceu no ano {anoNasc1}")
"""

"""
4)
numero1 = float(input("Informe o 1° número:"))
numero2 = float(input("Informe o 2° número:"))
numero3 = float(input("Informe o 3° número:"))

if numero1 > numero2 and numero1 > numero3:
    print(f"O número {numero1} é o maior número")
elif numero2 > numero1 and numero2 > numero3:
    print(f"O número {numero2} é o maior número")
else:
    print(f"O número {numero3} é o maior número")
"""

"""
5)
nome = input("Informe seu nome:")
prova1 = float(input("Informe a nota da sua 1° prova:"))
prova2 = float(input("Informe a nota da sua 2° prova:"))
media = round((prova1 + prova2 ) / 2,2)
print(f"Sua média foi de {media}")
if media >= 0 and media < 5:
    print("Reprovado")
elif media >= 5 and media < 7:
    print("Recuperação")
elif media >= 7 and media <= 10:
    print("Aprovado")
else:
    print("Algo deu errado!")
"""

"""
6)
media = float(input("Qual foi sua média?"))
faltas = int(input("Qual foi a sua quantidade de faltas?"))
if media >= 7 and faltas <= 32:
    print("Aprovado")
elif media < 7 and faltas <= 32:
    print("Reprovado por média")
elif media >= 7 and faltas > 32:
    print("Reprovado por falta")
else:
    print("Reprovado por média e falta")
"""

"""
7)
angulo1 = float(input("Qual o valor do seu 1° ângulo?"))
angulo2 = float(input("Qual o valor do seu 2° ângulo?"))
angulo3 = float(input("Qual o valor do seu 3° ângulo?"))
triangulo = angulo1 + angulo2 + angulo3

if triangulo == 180:
    if angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
        print("Este é um Triângulo Acutângulo")
    elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
        print("Este é um Triângulo Retângulo")
    elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
        print("Este é um Triângulo Obtusângulo")
else:
    print("Os ângulos informados não formam um triângulo")
"""

"""
8)
km = float(input("Qual a distância em Km que você percorreu?"))
litros = float(input("Quantos litros você gastou no percurso?"))
consumo = round(km / litros,2)
if consumo < 8: 
    print("Venda o carro!")
elif consumo >= 8 and consumo <= 14:
    print("Econômico!")
else:
    print("Super Econômico!")
"""

"""
9)
print("1 - Homem")
print("2 - Mulher")
escolha = int(input("Faça sua escolha digitando o número:"))
if escolha == 1:
    pesoH = float(input("Qual seu peso?"))
    alturaH = float(input("Qual sua altura em centímetros?"))
    idadeH = int(input("Qual sua idade?"))
    calDiaH = round(66 + (13.7 * pesoH) + (5 * alturaH) - (6.8 * idadeH))
    print(f"A sua quantidade de consumo ideal de calorias é de {calDiaH}")
elif escolha == 2:
    pesoM = float(input("Qual seu peso?"))
    alturaM = float(input("Qual sua altura em centímetros?"))
    idadeM = int(input("Qual sua idade?"))
    calDiaM = round(66.5 + (9.6 * pesoM) + (1.8 * alturaM) - (4.7 * idadeM),2)
    print(f"A sua quantidade de consumo ideal de calorias é de {calDiaM}")

else:
    print("Algo deu errado!")
"""

"""
10)
salario = float(input("Qual seu salário?"))

if salario <= 1903.98: 
    print("Você está isento de imposto")
    print(f"Seu salário liquido é de {salario}")
elif salario > 1903.98 and salario <= 2826.65:
    imposto = round((salario * 0.075) - 142.80,2)
    print(f"Seu salário liquido é de R${imposto}")
elif salario > 2826.65 and salario <= 3751.05:
    imposto = round((salario * 0.15) - 548.82,2)
    print(f"Seu salário liquido é de R${imposto}")
elif salario > 3751.05 and salario < 4664.68:
    imposto = round((salario * 0.225) - 636.13,2)
    print(f"Seu salário liquido é de R${imposto}")
elif salario > 4664.68:
    imposto = round((salario * 0.275) - 869.36,2)
    print(f"Seu salário liquido é de R${imposto}")
"""

"""
11)
mes = int(input("Qual o mês (digite o número do mês)?"))
ano = input("Qual o ano?")

segundaPartAno = int(ano[2:])
if segundaPartAno % 4 == 0:
    diasMes = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if 1 <= mes <= 12:
        dias = diasMes[mes - 1]
        print(f"O mês {mes} tem {dias}")
    else:
        print("Mês inválido")
else:
    diasMes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if 1 <= mes <= 12:
        dias = diasMes[mes - 1]
        print(f"O mês {mes} tem {dias}")
    else:
        print("Mês inválido")
"""

"""
12)
sexo = input("Qual seu sexo?")
idade = int(input("Qual sua idade?"))

if sexo.lower() == "masculino" and idade >= 21:
    print("Maior de idade")
elif sexo.lower() == "feminino" and idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
"""

"""
13)
hasteAco = int(input("Quantas hastes de aço você querer levar?"))
hasteCobre = int(input("Quantas hastes de cobre você querer levar?"))
hasteAl = int(input("Quantas hastes de alumínio você querer levar?"))

valorHastes = (hasteAco * 2.5) + (hasteCobre * 4) + (hasteAl * 5)
qtdHastes = hasteAco + hasteCobre + hasteAl

if qtdHastes < 6:
    print(f"O valor total das hates é R${valorHastes}")
elif qtdHastes >= 7 and qtdHastes <= 15:
    desconto = valorHastes * 0.1
    print(f"O valor total das hates é R${desconto}")
elif qtdHastes >= 16 and qtdHastes < 20:
    desconto = valorHastes * 0.15
    print(f"O valor total das hates é R${desconto}")
else:
    desconto = valorHastes * 0.2
    print(f"O valor total das hates é R${desconto}")
"""

"""
14)
print("Qual tipo de consumidor você é?")
print("I - Industrial")
print("C - Comercial")
print("R - Residencial")
escolha = input("Digite a letra correspondente:")
qtdEnergia = float(input("Qual a quantidade de energia consumida?"))

if escolha.lower() == "i":
    vPago = round((0.68 * qtdEnergia) + 34,2)
    print(f"O valor a ser pago é de R${vPago}")
elif escolha.lower() == "c":
    vPago = round((0.37 * qtdEnergia) + 45,2)
    print(f"O valor a ser pago é de R${vPago}")
elif escolha.lower() == "r":
    vPago = round((0.77 * qtdEnergia) - 22,2)
    print(f"O valor a ser pago é de R${vPago}")
else:
    print("Algo deu errado, tente novamente!")
"""

"""
15)
# Pede a hora e o minuto inicial
horaI = int(input("Qual foi a hora inicial do jogo?"))
minutoI = int(input("Qual foi o minuto inicial do jogo?"))

# Pede a hora e o minuto final
horaF = int(input("Qual a hora final do jogo?"))
minutoF = int(input("Qual o minuto final do jogo?"))

# Evita que o usuário insira horarios inesistentes
if horaI <= 24 and minutoI <= 59:
    # A mesma coisa
    if horaF <= 24 and minutoF <= 59:
        # Transforma o tempo inicial e final em minutos
        tempoI = (horaI * 60) + minutoI
        tempoF = (horaF * 60) + minutoF
        # Correção de erro para se caso o horario de fim passe da meia noite
        if tempoF < tempoI:
            tempoF += 24 * 60
        # Calculo final
        duracaoEmMin = tempoF - tempoI
        duracacoH = duracaoEmMin // 60  # // - Usado para pegar apenas a parte inteira da divisão
        duracaoMin = duracaoEmMin % 60
        print(f"O jogo a cabou as {duracacoH} horas e {duracaoMin} minutos")
    else:
        print("Entrada de dados não valida")
else:
    print("Entrada de dados não valida")
"""

"""
16)
numero = int(input("Digite um número inteiro de 3 dígitos:"))
centena = numero // 100
dezena = numero % 100
casaD = dezena // 10
casaUnidade = dezena % 10
soma = centena + casaD + casaUnidade

if 16 % soma == 0 and soma % 4 == 0:
    print("O número é divisor de 16 e múltiplo de 4 ao mesmo tempo")
else:
    print("Ele não nem divisor de 16 nem múltiplo de 4!")
"""

"""
17)
print("y = 7x^3 - 3x^0.5 - 8t / 5 (x + 1)")
z = float(input("Atribua um valor a Z:"))
w = float(input("Atribua um valor a W:"))

if w > 0 or z < 7:
    x = round(((5 * w) + 1) / 3,2)
    t = round((5 * z) + 2,2)
else:
    x = round((5 * z) + 2,2)
    t = round((5 * w) + 1 / 3,2)

y = round(((7 * x) ** 3) - ((3 * x) ** 0.5) - (8 * t) / (5 * (x + 1)),2)
print(f"O valor de y é {y}")
"""