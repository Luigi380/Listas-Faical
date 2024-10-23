"""
1)
vDolar = 3.12
vReal = float(input("Quantos reais você tem?"))
cambio = round(vReal / vDolar,2)
print(f"Você tem US${cambio} em dolar")
"""

"""
2)
vReal = 3.12
vDolar = float(input("Quantos dolares você tem?"))
cambio = round(vDolar * vReal,2)
print(f"Você tem R${cambio} em reais")
"""

"""
3)
alturaP = float(input("Qual a altura da parede em metros?"))
larguraP = float(input("Qual a largura da parede em metros?"))

alturaZ = float(input("Qual a altura dos azulejos em centimetros?"))
larguraZ = float(input("Qual a largura dos azulejos em centimetros?"))
conversaoAz = round(alturaZ / 100, 2)
conversaoLz = round(larguraZ / 100, 2)

areaP = round(alturaP * larguraP,2)
areaZ = round(conversaoAz* conversaoLz,2)

resultado = round(areaP / areaZ,2)
print(f"Você vai precisar de {resultado} azulejos")
"""

"""
4)
ladoA = float(input("Qual a altura do retângulo?"))
ladoB = float(input("Qual a largura do retângulo?"))

areaR = round(ladoA * ladoB, 2)
perimetroR = round((2 * ladoA) + (2 * ladoB), 2)
print(f"O retângulo tem uma área de {areaR}")
print(f"O retângulo tem um perimetro de {perimetroR}")
"""

"""
5)
peso = float(input("Quanto você pesa?"))
altura = float(input("Qual sua altura?"))
imc = round(peso / (altura * altura),2)
print(f"Seu IMC é de {imc}")
"""

"""
6)
raio = float(input("Qual o Raio da esfera?"))
volume = round((4 / 3) * (raio * raio * raio), 2)
area = round(4 * (raio * raio), 2)
print(f"O volume da sua esfera é de {volume} πcm³")
print(f"A área da sua esfera é de {area} πcm²")
"""

"""
7)
prova1 = float(input("Qual sua nota na prova 1?"))
prova2 = float(input("Qual sua nota na prova 2?"))
atv = float(input("Qual sua nota na ATV?"))
media = round((4 * prova1) + (3 * prova2) + (2 * atv) / 9, 2)
print(f"A sua média foi de {media}")
"""

"""
8)
s0 = 2
v0 = 3
a = 10
temp = float(input("Em quanto tempo o espaço foi percorrido em segundos?"))
espaco = round(s0 + (v0 * temp) + (1 / 2) * (a * (temp * temp)),2)
print(f"O espaço percorrido foi de {espaco}")
"""

"""
9)
vMacas = 1.30
vBanana = 5
qMacas = int(input("Quantas maçãs você comprou?"))
kgBanana = float(input("Quantos kg de banana você comprou?"))
total = round((qMacas * vMacas) + (kgBanana * vBanana),2)
print(f"Sua compra deu um total de R${total}")
"""

"""
10)
diasMes = 30
diasAno = 365

diaNasc = int(input("Em que dia você nasceu?"))
mesNasc = int(input("Em que mês você nasceu?"))
anoNasc = int(input("Em que ano você nasceu?"))

dia = int(input("Em que dia você está?"))
mes = int(input("Em que mês você está?"))
ano = int(input("Em que ano você está?"))

diasAnoNascido = (anoNasc * diasAno) + (mesNasc * diasMes) + diaNasc
diasAnoAtual = (ano * diasAno) + (mes * diasMes) + dia
totalDias = diasAnoAtual - diasAnoNascido
print(f"Você tem {totalDias} dias de vida")
"""

"""
11)
percDistribuidor = 0.28
percImposto = 0.45

custoFabrica = float(input("Qual o custo de fabricação do carro?"))

custosDistribuidor = custoFabrica * percDistribuidor
custosImposto = custoFabrica * percImposto

custoFinal = custosDistribuidor + custosImposto + custoFabrica
print(f"O custo ao consumidor é de R${custoFinal}")
"""

"""
12)
qtdCarrosVendidos = int(input("Quantos carros foram vendidos?"))
totalVendas = float(input("Qual o valor total de vendas?"))
slarioFixo = float(input("Qual o salario fixo?"))
valorComissao = float(input("Qual o valor da comissão por carro vendido?"))

slarioFinal = slarioFixo + (valorComissao * qtdCarrosVendidos) + ((5 * totalVendas) / 100)
print(f"O salario final do vendedor é de R${slarioFinal}")
"""