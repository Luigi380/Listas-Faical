def q1():
    lista = []
    for i in range(100):
        if i % 2 == 0:
            lista.append(0)
        else:
            lista.append(1)
    print(lista)

def q2():
    lista1 = list(range(5))
    lista2 = list(range(10))
    lista3 = lista1 + lista2
    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")
    print(f"Lista 3: {lista3}")
q2()