from grafo import *



class Main:
    def __init__(self):

        # Criação de um grafo
        self.grafo = Grafo()

        #teste criação do grafo
        self.grafo.criarGrafo(3)  # Criar grafo com 5 vértices

        #teste grafo aleatório
        #self.grafo.criarGrafoAleatorio(3, 10, 2, 10)
        #print("breakpoint ...................................")
        #teste adicionar arestas
        self.grafo.adicionaArcoNaoDirigido("V1", "V2", 2)
        #self.grafo.adicionaArcoNaoDirigido("V4", "V5", 3)
        #self.grafo.adicionaArcoNaoDirigido("V5", "V1", 3)
        #self.grafo.adicionaArcoDirigido("V4", "V5")

        #teste ponderação e rotulação de vértices
        #self.grafo.ponderarERotularVertice("V1", 10, "A1")
        #self.grafo.ponderarERotularVertice("V2", 15, "A2")

        #teste ponderação e rotulação de arestas
        #self.grafo.ponderarERotularAresta("V1", "V2", 7, "R1")

        #teste remoção de arco
        #self.grafo.removeArco("V1", "V2")

        #teste verificar a existência de uma aresta
        #self.grafo.existeAresta("V1", "V2")

        #teste exibindo o grafo em diferentes representações
        # self.grafo.mostrarVertices()
        # self.grafo.mostrarListaAdjacencia()
        # self.grafo.mostrarMatrizAdjacencia()
        # self.grafo.mostrarMatrizIncidencia()

        #teste verificando se o grafo é vazio
        #self.grafo.ehVazio()

        #teste verificando se o grafo é completo
        #self.grafo.ehCompleto()

        #teste verificando conectividade simples
        #self.grafo.checarConectividadeSimples()

        #teste verificando conectividade semifortemente
        #self.grafo.checarConectividadeSemifortemente()

        #teste verificando conectividade fortemente
        #self.grafo.checarConectividadeFortemente()

        # self.grafo = Grafo()
        # self.grafo.criarGrafo(3)
        # self.grafo.adicionaArcoNaoDirigido("V1", "V2", 5)
        # self.grafo.adicionaArcoNaoDirigido("V2", "V3", 3)
        # self.grafo.ponderarERotularAresta("V1", "V2", 7, "R1")
        # self.grafo.ponderarERotularVertice("V1", 10, "A1")
        # self.grafo.ponderarERotularVertice("V2", 11, "A3")

        self.grafo=Grafo()
        self.grafo.criarGrafoAleatorio(9,9,36,47)
        #self.grafo.metodo_tarjan_direcionado()
        #self.grafo.verificarPontes()
        self.grafo.exibirCaminhoEulerianoDFS()
       
        self.grafo.exportarParaGraphML("grafo2.GRAPHML")
if __name__ == "__main__":
    main = Main()

