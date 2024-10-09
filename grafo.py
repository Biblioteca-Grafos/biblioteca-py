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

##Consegui criar um grafo nao direcionado
def main():
    print("________________________________");
    print("Aqui começa o grafo não direcionado");
    grafoNDir = GrafoNaoDirecionado();
    grafoNDir.adicionarVertice("A");
    grafoNDir.adicionarVertice("B");
    grafoNDir.adicionarVertice("C");
    grafoNDir.adicionarAresta("A","B");
    grafoNDir.adicionarAresta("B","C");
    print("Mostrando meu grafo");
    grafoNDir.mostrarGrafo();

    print("________________________________");
    print("Aqui começa o grafo direcionado");
    grafoDir = GrafoDirecionado();
    grafoDir.adicionarVertice("Belo Horizonte");
    grafoDir.adicionarVertice("Contagem das Aboboras");
    grafoDir.adicionarAresta("Belo Horizonte", "Contagem das Aboboras");
    grafoDir.adicionarVertice("Betim");
    grafoDir.adicionarAresta("Contagem das Aboboras", "Betim");
    print("Mostrando meu grafo");
    grafoDir.mostrarGrafo();
    print("________________________________");
if __name__ == "__main__":
    main()

