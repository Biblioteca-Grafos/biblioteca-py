from grafo import * 

def criarGrafoNDirecionado(grafo):
    print("/////////////////////////////////")
    print("Criaçao grafo Não direcionado\n")
    quantidadeVertices = int(input("Primeiro, selecione quantos vértices possuirá: "))

    for i in range(quantidadeVertices):
        vertice = input(f"Insira o vértice {i + 1}: ")
        grafo.adicionarVertice(vertice)

    while(True):
        adicionaAresta = input("Deseja adicionar algum vértice? y/n ")

        if adicionaAresta == "n" or adicionaAresta == "N":
            print("Seu grafo foi criado com sucesso!")
            grafo.mostrarListaAdjacencia()
            print("")
            return

        print("Escolha um vertice primeiro")
        grafo.mostrarVertices()
        inputPrimeiroVertice = input("=> ")

        if inputPrimeiroVertice not in grafo.grafo:
            print("Por favor selecione um vertice valido")
            continue

        print("Escolha o segundo vértice para a aresta:")
        grafo.mostrarVertices()
        inputSegundoVertice = input("=> ")

        if inputSegundoVertice not in grafo.grafo:
            print("O vértice escolhido não existe. Tente novamente.")
            continue

        grafo.adicionarAresta(inputPrimeiroVertice, inputSegundoVertice)


        break


