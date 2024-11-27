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
                grafo.ponderarERotularVertice("V1", 2, "VERTICE 1")
                grafo.ponderarERotularVertice("V2", 3, "VERTICE 2")
                grafo.ponderarERotularAresta("V1", "V2", 3, "ARESTA 1")
                grafo.mostrarListaAdjacencia()
                print("Teste passou.")
                grafo.exportarParaGraphML("teste.GRAPHML")
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

        def menu():
            print("Bem-vindo ao sistema de criação de grafos!")

            while True:
                print("\n______________________________________________________")
                print("Menu Inicial")
                print("Escolha uma opção:")
                print("1. Criar Grafo Aleatório Não Direcionado")
                print("2. Criar Grafo Linear Direcionado")
                print("3. Importar Grafo")
                print("0. Sair")

                opcao = input("> ")

                if opcao == "1":
                    # Criar grafo aleatório não direcionado
                    print("Defina o número de vértices:")
                    vertices = int(input("> "))
                    print("Defina o número mínimo de arestas:")
                    minArestas = int(input("> "))
                    print("Defina o número máximo de arestas:")
                    maxArestas = int(input("> "))
                    
                    ehDirecionado = False

                    grafo = Grafo()
                    grafo.criarGrafoAleatorio(vertices, vertices, minArestas, maxArestas)
                    grafo.mostrarListaAdjacencia()

                elif opcao == "2":
                    # Criar grafo linear direcionado
                    print("Defina o número de vértices para o grafo linear direcionado:")
                    numVertices = int(input("> "))
                    ehDirecionado = True

                    grafo = Grafo()
                    grafo.criarGrafoLinearDirecionado(numVertices)
                    grafo.mostrarListaAdjacencia()

                elif opcao == "3":
                    grafo = Grafo()
                    grafo.importarDeGraphML("grafo.graphml")
                    grafo.mostrarListaAdjacencia() 

                elif opcao == "0":
                    print("Saindo do programa.")
                    break

                else:
                    print("Opção inválida. Tente novamente.")

                # Submenu de funcionalidades para o grafo criado
                while True:
                    print("\n______________________________________________________")
                    print("Menu de funcionalidades")
                    print("Escolha uma opção:")
                    print("1. Ver Matriz de Adjacência")
                    print("2. Ver Matriz de Incidência")
                    print("3. Ver Lista de Adjacência")
                    print("4. Ponderar vértice")
                    print("5. Ponderar aresta")
                    print("6. Checagem de adjacência entre vértices")
                    print("7. Checagem de adjacência entre arestas")
                    print("8. Checagem da existência de arestas")
                    print("9. Checagem da quantidade de vértices e arestas")
                    print("10. Checagem de grafo vazio e completo")
                    print("11. Verificar se é simplesmente conexo")
                    print("12. Verificar se é semifortemente conexo")
                    print("13. Verificar se é fortemente conexo")
                    print("14. Kosaraju")
                    print("15. Checagem de ponte e articulação")
                    print("16. Naive")
                    print("17. Tarjan")
                    print("18. Fleury")
                    print("19. Exportar")
                    print("0. Voltar ao Menu Inicial")

                    funcionalidade = input("> ")

                    if funcionalidade == "1":
                        grafo.mostrarMatrizAdjacencia()
                    elif funcionalidade == "2":
                        grafo.mostrarMatrizIncidencia()
                    elif funcionalidade == "3":
                        grafo.mostrarListaAdjacencia()
                    elif funcionalidade == "4":
                        vertice = input("Digite o vértice para ponderar: ")
                        valor_ponderacao = float(input("Digite o valor da ponderação: "))
                        rotulo = input("Digite o rótulo: ")
                        grafo.ponderarERotularVertice(vertice, valor_ponderacao, rotulo)
                    elif funcionalidade == "5":
                        a = input("Digite o primeiro vértice da aresta: ")
                        b = input("Digite o segundo vértice da aresta: ")
                        valor_ponderacao = float(input("Digite o valor da ponderação: "))
                        rotulo = input("Digite o rótulo: ")
                        grafo.ponderarERotularAresta(a, b, valor_ponderacao, rotulo)
                    elif funcionalidade == "6":
                        a = input("Digite o primeiro vértice: ")
                        b = input("Digite o segundo vértice: ")
                        grafo.verificarAdjacencia(a, b)
                    elif funcionalidade == "7":
                        grafo.verificarAdjacenciaEntreArestas()
                    elif funcionalidade == "8":
                        a = input("Digite o primeiro vértice: ")
                        b = input("Digite o segundo vértice: ")
                        grafo.existeAresta(a, b)
                    elif funcionalidade == "9":
                        grafo.quantidadeVertices()
                        grafo.quantidadeArestas()
                    elif funcionalidade == "10":
                        grafo.ehVazio()
                        grafo.ehCompleto()
                    elif funcionalidade == "11":
                        grafo.checarConectividadeSimples()
                    elif funcionalidade == "12":
                        grafo.checarConectividadeSemifortemente()
                    elif funcionalidade == "13":
                        grafo.checarConectividadeFortemente()
                    elif funcionalidade == "14":
                        componentes = grafo.kosaraju()
                        print("Componentes fortemente conexos:", componentes)
                    elif funcionalidade == "15":
                        grafo.encontrarPonteEArticulacao(ehDirecionado)
                    elif funcionalidade == "16":
                        grafo.verificarPontes()
                    elif funcionalidade == "17":
                        grafo.metodo_tarjan_direcionado()
                    elif funcionalidade == "18":
                        grafo.exibirCaminhoEulerianoDFS()
                    elif funcionalidade == "19":
                        grafo.exportarParaGraphML("grafo.GRAPHML", ehDirecionado)
                    elif funcionalidade == "0":
                        break
                    else:
                        print("Opção inválida. Tente novamente.")


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
        # testeAdicionarArestaDirigida()
        # testeEuleriano()
        menu()
        

if __name__ == "__main__":
    main = Main()