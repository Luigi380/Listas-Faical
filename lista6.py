def q1():
    lista = []
    for i in range(100):
        if i % 2 == 0:
            lista.append(0)
        else:
            lista.append(1)
    print(lista)


def q2():
    lista1 = []
    lista2 = []
    for i in range(5):
        num = int(input("Insira um número para a lista 1:"))
        lista1.append(num)
    print("--------------------------------------")
    for j in range(10):
        num = int(input("Insira um número para a lista 2:"))
        lista2.append(num)
    lista3 = lista1 + lista2
    print("--------------------------------------")
    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")
    print(f"Lista 3: {lista3}")


def q3():
    listaNotas = []
    listaMatriculas = []
    notas = 0
    qtdDeAlunos = int(input("Quantos alunos querem ver suas notas?"))
    for i in range(qtdDeAlunos):
        matriculas = input("Qual a matricula?")
        listaMatriculas.append(matriculas)
        for j in range(5):
            notas = float(input("Informe suas notas:"))
            listaNotas.append(notas)
            print(f"As notas do aluno de matricula {listaMatriculas[i]} tem as notas {listaNotas}")

        
q3()