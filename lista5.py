import os
os.system('cls')


"""
1)
num = int(input("Insira números inteiros positivos, quando desejar parar digite o número 0: "))
contNum = 0
contLidos = 0
while num != 0:
    if num >= 10 and num <= 50:
        contLidos += 1
    else:
        contNum += num
    num = int(input("Insira números inteiros positivos, quando desejar parar digite o número 0: "))
print(f"A quantidade de números lidos entre 10 e 50 é: {contLidos}")
print(f"A soma dos números lidos que não estão entre 10 e 50 é: {contNum}")
"""

"""
2)
i = 101
while i > 10:
    i -= 2
    if i < 10:
        break
    print(i)
"""

"""
3)
while True:
    num = int(input("Insira números inteiros positivos, quando desejar parar digite o número 0: "))
    if num == 0:
        break
    if num % 13 == 2:
        print(f"{num} quando divido por 13 da resto 2")
"""

"""
4)
num = int(input("Insira números inteiros positivos, quando desejar parar digite um número negativo: "))
cont10 = 0
cont5 = 0
cont2 = 0
contNum = 0
while num >= 0:
    if num % 10 == 0:
        cont10 += 1
    elif num % 5 == 0:
        cont5 += 1
    elif num % 2 == 0:
        cont2 += 1
    else:
        contNum += 1
    num = int(input("Insira números inteiros positivos, quando desejar parar digite um número negativo: "))
print(f"A quantidade de números que são divisiveis por 10 é: {cont10}")
print(f"A quantidade de números que são divisiveis por 5 é: {cont5}")
print(f"A quantidade de números que são divisiveis por 2 é: {cont2}")
print(f"A quantidade de números que não são divisiveis por nenhum desses números é: {contNum}")
"""

"""
5)
total_salarios = 0
quantidade_pessoas = 0
menor_salario = float('inf')
maior_idade = -float('inf')
menor_idade = float('inf')
quantidade_mulheres = 0
idade_menor_salario = -1
sexo_menor_salario = ''

while True:
    idade = int(input("Digite a idade (ou idade negativa para finalizar): "))
    
    if idade < 0:
        break
    
    sexo = input("Digite o sexo (M/F): ")
    salario = float(input("Digite o salário: "))
    
    total_salarios += salario
    quantidade_pessoas += 1
    
    if sexo.lower() == 'f':
        quantidade_mulheres += 1
    
    if idade > maior_idade:
        maior_idade = idade
    if idade < menor_idade:
        menor_idade = idade
    
    if salario < menor_salario:
        menor_salario = salario
        idade_menor_salario = idade
        sexo_menor_salario = sexo

if quantidade_pessoas > 0:
    media_salarios = round(total_salarios / quantidade_pessoas,2)
    print(f"\nMédia dos salários: R$ {media_salarios}")
    print(f"Maior idade do grupo: {maior_idade}")
    print(f"Menor idade do grupo: {menor_idade}")
    print(f"Quantidade de mulheres: {quantidade_mulheres}")
    print(f"Idade e sexo da pessoa com o menor salário: {idade_menor_salario} anos, {sexo_menor_salario.upper()}")
else:
    print("Nenhuma pessoa foi cadastrada.")
"""
