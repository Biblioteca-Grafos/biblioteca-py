from grafo import *

def criarGrafoNDirecionado(grafo):
    print("/////////////////////////////////")
    print("Criação grafo Não direcionado\n")
    quantidadeVertices = int(input("Primeiro, selecione quantos vértices possuirá: "))

    for i in range(quantidadeVertices):
        vertice = input(f"Insira o vértice {i + 1}: ")
        grafo.adicionarVertice(vertice)

    while True:
        adicionaAresta = input("Deseja adicionar alguma aresta? y/n ")

        if adicionaAresta.lower() == "n":
            print("Seu grafo não direcionado foi criado com sucesso!")
            grafo.mostrarListaAdjacencia()
            print("")
            return

        print("Escolha o primeiro vértice:")
        grafo.mostrarVertices()
        inputPrimeiroVertice = input("=> ")

        if inputPrimeiroVertice not in grafo.grafo:
            print("Por favor selecione um vértice válido.")
            continue

        print("Escolha o segundo vértice:")
        grafo.mostrarVertices()
        inputSegundoVertice = input("=> ")

        if inputSegundoVertice not in grafo.grafo:
            print("O vértice escolhido não existe. Tente novamente.")
            continue

        peso = int(input(f"Digite o peso da aresta entre {inputPrimeiroVertice} e {inputSegundoVertice} (padrão 1): ") or 1)

        grafo.adicionarAresta(inputPrimeiroVertice, inputSegundoVertice, peso)

        print(f"Aresta adicionada entre {inputPrimeiroVertice} e {inputSegundoVertice} com peso {peso}.\n")


def criarGrafoDirecionado(grafo):
    print("/////////////////////////////////")
    print("Criação grafo Direcionado\n")
    quantidadeVertices = int(input("Primeiro, selecione quantos vértices possuirá: "))


    for i in range(quantidadeVertices):
        vertice = input(f"Insira o vértice {i + 1}: ")
        grafo.adicionarVertice(vertice)

    while True:
        adicionaAresta = input("Deseja adicionar alguma aresta? y/n ")

        if adicionaAresta.lower() == "n":
            print("Seu grafo direcionado foi criado com sucesso!")
            grafo.mostrarListaAdjacencia()
            print("")
            return

        print("Escolha um vértice de origem:")
        grafo.mostrarVertices()
        inputOrigem = input("=> ")

        if inputOrigem not in grafo.grafo:
            print("Por favor selecione um vértice válido.")
            continue

        print("Escolha um vértice de destino:")
        grafo.mostrarVertices()
        inputDestino = input("=> ")

        if inputDestino not in grafo.grafo:
            print("O vértice escolhido não existe. Tente novamente.")
            continue

        peso = int(input(f"Digite o peso da aresta de {inputOrigem} para {inputDestino} (padrão 1): ") or 1)

        grafo.adicionarAresta(inputOrigem, inputDestino, peso)

        print(f"Aresta direcionada adicionada de {inputOrigem} para {inputDestino} com peso {peso}.\n")
