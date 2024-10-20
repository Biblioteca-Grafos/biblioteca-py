###########################################################################################################
class Grafo:
    def __init__(self):
        self.grafo = {}
        self.arestas = []

    def adicionarVertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

##funcoes para exibir o grafo##
    def mostrarVertices(self):
        print("Mostrando todos os vertices do Grafo")
        for vertice in self.grafo:
            print(f"{vertice}")
        print("Fim mostrando todos os vertices do Grafo\n")

    def mostrarArestas(self):
        print("Mostrando todas as arestas")
        for aresta in self.arestas:
            print(f"teste{aresta}")
        print("Fim mostrando todas as arestas\n")


    def mostrarListaAdjacencia(self):
        print("Representando Grafo com Lista de Adjacencia")
        for vertice in self.grafo:
            print(f"{vertice}: {self.grafo[vertice]}") 
        print("Fim representando Grafo com Lista de Adjacencia\n")

    def mostrarMatrizAdjacencia(self):
        listaVertices = list(self.grafo.keys())
        quantVertices = len(listaVertices)
        minhaMatriz = [[0] * quantVertices for _ in range(quantVertices)]

        for i, vertice1 in enumerate(listaVertices):
            for vertice2, peso in self.grafo[vertice1]:
                j = listaVertices.index(vertice2)
                minhaMatriz[i][j] = peso

        print("Representando Grafo com Matriz de Adjacencia")
        print("  "," ".join(listaVertices))
        for i in range(quantVertices):
            linha = [str(minhaMatriz[i][j]) for j in range (quantVertices)]
            print(f"{listaVertices[i]} " + " ".join(linha))
        print("Fim representando Grafo com Matriz de Adjacencia\n")


    def mostrarMatrizIncidencia(self):
        listaVertices = list(self.grafo.keys())
        quantVertices = len(listaVertices)
        quantArestas = len(self.arestas)
        minhaMatriz = [[0] * quantArestas for _ in range (quantVertices)] 
        
        for i, (vertice1, vertice2, peso) in enumerate(self.arestas):
            j = listaVertices.index(vertice1)
            k = listaVertices.index(vertice2)
            minhaMatriz[j][i] = 1
            minhaMatriz[k][i] = 1

        print("Representando Grafo com Matriz de Incidencia")
        print(" ", " ".join(f"E{index+1}" for index in range(quantArestas)))
        for i in range(quantVertices):
            linha = [str(minhaMatriz[i][j]) for j in range(quantArestas)]
            print(f"{listaVertices[i]} " + " ".join(linha))
        print("Fim representando Grafo com Matriz de Incidencia\n")
###########################################################################################################


###########################################################################################################
class GrafoNaoDirecionado(Grafo):
    def adicionarAresta(self, vertice1, vertice2, peso = 1):
        if vertice1 in self.grafo and vertice2 in self.grafo:
            self.grafo[vertice1].append((vertice2, peso))
            self.grafo[vertice2].append((vertice1, peso))
            self.arestas.append((vertice1, vertice2, peso))

    def removerAresta(self, vertice1, vertice2):
        if vertice1 in self.grafo and vertice2 in self.grafo:
            self.grafo[vertice1] = [(v, p) for v, p in self.grafo[vertice1] if v != vertice2]
            self.grafo[vertice2] = [(v, p) for v, p in self.grafo[vertice2] if v != vertice1]
            self.arestas = [(v1, v2, p) for v1, v2, p in self.arestas if (v1, v2) != (vertice1, vertice2) and (v2, v1) != (vertice1, vertice2)]
###########################################################################################################

###########################################################################################################
class GrafoDirecionado(Grafo):
    def adicionarAresta(self, origem, destino, peso=1):
        if origem in self.grafo and destino in self.grafo:
            self.grafo[origem].append((destino, peso))  # Corrigido: passando tupla (destino, peso)
            self.arestas.append((origem, destino, peso))

    def removerAresta(self, origem, destino):
        if origem in self.grafo and destino in self.grafo:
            self.grafo[origem] = [(v, p) for v, p in self.grafo[origem] if v != destino]

###########################################################################################################

