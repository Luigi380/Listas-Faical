import time

def removerSimbolos(texto):
    espaço = ' '
    for i in texto:
        if i.isalpha():
            espaço += i
        else:
            espaço += ' '
    return espaço.strip()

def selecionarPalavras(conteudo):
    listaFile = removerSimbolos(conteudo).lower().split()
    return listaFile

def carregarPalavrasArquivo():
    with open (file_path, 'r') as arquivo:
        conteudo = arquivo.read()
    return selecionarPalavras(conteudo)

def frequenciaPalavrasDicionario():
    inicio = time.perf_counter()

    dicionarioDeFrequencia = {}

    for palavra in carregarPalavrasArquivo():
        if palavra in dicionarioDeFrequencia:
            dicionarioDeFrequencia[palavra] += 1
        else:
            dicionarioDeFrequencia[palavra] = 1
    print(dicionarioDeFrequencia)

    fim = time.perf_counter()

    execução = fim - inicio
    print(f"O tempo de execução é de {execução:.5f} segundos")
    salvaListaArquivo(dicionarioDeFrequencia, execução)

    return dicionarioDeFrequencia

def salvaListaArquivo(dicionario, tempo):
    with open("frequencias.txt", "w") as f:
        f.write(f"O tempo foi de {tempo:.5f} segundos \n")
        for palavra, frequencia in dicionario.items():
            f.write(f"{palavra} : {frequencia}\n")

file_path = 'alice.txt'
frequenciaPalavrasDicionario()
