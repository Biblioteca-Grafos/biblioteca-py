class Grafo:
    def __init__(self):
        self.grafo = {}

    def adicionarVertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []
    
    def mostrarGrafo(self):
        for vertice in self.grafo:
            print(f"{vertice}: {self.grafo[vertice]}") 


class GrafoNaoDirecionado(Grafo):
    def adicionarAresta(self, vertice1, vertice2):
        if vertice1 in self.grafo and vertice2 in self.grafo:
            self.grafo[vertice1].append(vertice2)
            self.grafo[vertice2].append(vertice1)

class GrafoDirecionado(Grafo):
    def adicionarAresta(self, origem, destino):
        if origem in self.grafo and destino in self.grafo:
            self.grafo[origem].append(destino)

