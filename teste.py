from grafo import *



class Main:
    def __init__(self):
        def testeCriarGrafo():
            print("\n--- Teste criarGrafo ---")
            grafo = Grafo()
            grafo.criarGrafo(5)
            grafo.mostrarVertices()
            if len(grafo.grafo) == 5:
                print("Teste passou.")
            else:
                print("Teste falhou.")

        def testeAdicionarVertice():
            print("\n--- Teste adicionarVertice ---")
            grafo = Grafo()
            if grafo.adicionarVertice("V1") and "V1" in grafo.grafo:
                print("Teste passou.")
            else:
                print("Teste falhou.")

        def testeAdicionarArestaNaoDirigida():
            print("\n--- Teste adicionaArcoNaoDirigido ---")
            grafo = Grafo()
            grafo.criarGrafo(2)
            if grafo.adicionaArcoNaoDirigido("V1", "V2"):
                grafo.mostrarListaAdjacencia()
                print("Teste passou.")
            else:
                print("Teste falhou.")

        def testeAdicionarArestaDirigida():
            print("\n--- Teste adicionaArcoDirigido ---")
            grafo = Grafo()
            grafo.criarGrafo(2)
            if grafo.adicionaArcoDirigido("V1", "V2"):
                grafo.mostrarListaAdjacencia()
                print("Teste passou.")
            else:
                print("Teste falhou.")

        def testePonderarRotularVertice():
            print("\n--- Teste ponderarERotularVertice ---")
            grafo = Grafo()
            grafo.criarGrafo(1)
            if grafo.ponderarERotularVertice("V1", 10, "Inicial"):
                print("Teste passou.")
            else:
                print("Teste falhou.")

        def testePonderarRotularAresta():
            print("\n--- Teste ponderarERotularAresta ---")
            grafo = Grafo()
            grafo.criarGrafo(2)
            grafo.adicionaArcoNaoDirigido("V1", "V2")
            if grafo.ponderarERotularAresta("V1", "V2", 5, "Aresta 1"):
                print("Teste passou.")
            else:
                print("Teste falhou.")

        def testeRemoverAresta():
            print("\n--- Teste removeArco ---")
            grafo = Grafo()
            grafo.criarGrafo(2)
            grafo.adicionaArcoNaoDirigido("V1", "V2")
            grafo.removeArco("V1", "V2")
            if not grafo.existeAresta("V1", "V2"):
                print("Teste passou.")
            else:
                print("Teste falhou.")

        def testeConectividadeSimples():
            print("\n--- Teste checarConectividadeSimples ---")
            grafo = Grafo()
            grafo.criarGrafo(3)
            grafo.adicionaArcoNaoDirigido("V1", "V2")
            grafo.adicionaArcoNaoDirigido("V2", "V3")
            if grafo.checarConectividadeSimples():
                print("Teste passou.")
            else:
                print("Teste falhou.")

        def testeConectividadeFortemente():
            print("\n--- Teste checarConectividadeFortemente ---")
            grafo = Grafo()
            grafo.criarGrafo(3)
            grafo.adicionaArcoDirigido("V1", "V2")
            grafo.adicionaArcoDirigido("V2", "V3")
            grafo.adicionaArcoDirigido("V3", "V1")
            if grafo.checarConectividadeFortemente():
                print("Teste passou.")
            else:
                print("Teste falhou.")

        def testeKosaraju():
            print("\n--- Teste Kosaraju ---")
            grafo = Grafo()
            grafo.criarGrafo(3)
            grafo.adicionaArcoDirigido("V1", "V2")
            grafo.adicionaArcoDirigido("V2", "V3")
            grafo.adicionaArcoDirigido("V3", "V1")
            componentes = grafo.kosaraju()
            print(f"Componentes Fortemente Conexos: {componentes}")
            if len(componentes) == 1:
                print("Teste passou.")
            else:
                print("Teste falhou.")


        def testeEuleriano():
            print("\n Teste grafo euleriano")
            grafo = Grafo()
            grafo.criarGrafoAleatorio(11,109,111,122)
            grafo.exibirCaminhoEulerianoDFS()
            grafo.exportarParaGraphML("teste.GRAPHML")


        # # Executando todos os testes
        # testeCriarGrafo()
        # testeAdicionarVertice()
        # testeAdicionarArestaNaoDirigida()
        # testeAdicionarArestaDirigida()
        # testePonderarRotularVertice()
        # testePonderarRotularAresta()
        # testeRemoverAresta()
        # testeConectividadeSimples()
        # testeConectividadeFortemente()
        # testeKosaraju()
        # self.grafo.exportarParaGraphML("grafo2.GRAPHML")
        # testeEuleriano()


if __name__ == "__main__":
    main = Main()