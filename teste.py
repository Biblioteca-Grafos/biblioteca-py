from grafo import *


#     print("Iniciando testes do Grafo...\n")

#     # Criar instância do grafo
#     g = Grafo()

#     # Testando criação de vértices
#     print("TESTE: Adicionando vértices ao grafo")
#     g.criarGrafo(5)  # Adiciona V1, V2, V3, V4, V5
#     g.mostrarVertices()

#     # Testando adicionar arestas
#     print("TESTE: Adicionando arestas não direcionadas")
#     g.adicionaArcoNaoDirigido("V1", "V2")
#     g.adicionaArcoNaoDirigido("V2", "V3")
#     g.adicionaArcoNaoDirigido("V3", "V4")
#     g.adicionaArcoNaoDirigido("V4", "V5")
#     g.adicionaArcoNaoDirigido("V1", "V5")
#     g.mostrarListaAdjacencia()

#     # Testando arestas dirigidas
#     print("TESTE: Adicionando arestas direcionadas")
#     g.adicionaArcoDirigido("V5", "V1")
#     g.adicionaArcoDirigido("V3", "V1")
#     g.mostrarListaAdjacencia()

#     # Testando a existência de arestas
#     print("TESTE: Verificando existência de arestas")
#     g.existeAresta("V1", "V2")  # Deve ser True
#     g.existeAresta("V2", "V5")  # Deve ser False
#     g.existeAresta("V5", "V1")  # Deve ser True

#     # Testando remoção de arestas
#     print("TESTE: Removendo arestas")
#     g.removeArco("V1", "V2")
#     g.existeAresta("V1", "V2")  # Deve ser False
#     g.mostrarListaAdjacencia()

#     # Testando ponderação de vértices
#     print("TESTE: Ponderando vértices")
#     g.ponderarVertice("V1", 10)
#     g.ponderarVertice("V3", 20)

#     # Testando ponderação de arestas
#     print("TESTE: Ponderando arestas")
#     g.ponderarAresta("V2", "V3", 5)
#     g.ponderarAresta("V4", "V5", 15)
#     g.mostrarListaAdjacencia()

#     # Testando matrizes de adjacência e incidência
#     print("TESTE: Representação por Matriz de Adjacência")
#     g.mostrarMatrizAdjacencia()

#     print("TESTE: Representação por Matriz de Incidência")
#     g.mostrarMatrizIncidencia()

#     # Testando grafo aleatório
#     print("TESTE: Criando grafo aleatório")
#     g2 = Grafo()
#     g2.criarGrafoAleatorio(3, 6, 2, 5)
#     g2.mostrarListaAdjacencia()
#     g2.mostrarMatrizAdjacencia()
#     g2.mostrarMatrizIncidencia()

#     print("Todos os testes foram realizados com sucesso!")
# Criar grafo e adicionar vértices
# grafo = Grafo()

# # Teste com um grafo vazio
# grafo.ehVazio()  # Deve retornar True

# # Criar um grafo completo com 3 vértices
# grafo.criarGrafo(3)
# grafo.adicionaArcoNaoDirigido("V1", "V2")
# grafo.adicionaArcoNaoDirigido("V1", "V3")
# grafo.adicionaArcoNaoDirigido("V2", "V3")
# grafo.ehCompleto()  # Deve retornar True

# # Teste com um grafo incompleto
# grafo.removeArco("V1", "V2")
# grafo.ehCompleto()  # Deve retornar False



# grafo = Grafo()
# grafo.criarGrafo(3)
# grafo.adicionaArcoNaoDirigido("V1", "V2", 5)
# grafo.adicionaArcoNaoDirigido("V2", "V3", 10)
# grafo.ponderarERotularVertice("V1", 10, "Início")
# grafo.ponderarERotularVertice("V2", 20, "Meio")
# grafo.ponderarERotularAresta("V1", "V2", 5, "Conexão 1-2")

# # Exportar o grafo
# grafo.exportarParaGraphML("meu_grafo.graphml")\\


# Teste de exportação para GraphML
grafo = Grafo()

    # Criar 10 vértices
grafo.criarGrafo(10)

    # Ponderar e rotular vértices
for i in range(10):
    vertice = f"V{i+1}"
    grafo.ponderarERotularVertice(vertice, valor_ponderacao=i * 1.5, rotulo=f"Vertice {i+1}")

    # Adicionar arestas ponderadas e rotuladas
grafo.adicionaArcoNaoDirigido("V1", "V2", peso=2.0)
grafo.ponderarERotularAresta("V1", "V2", valor_ponderacao=2.0, rotulo="Aresta 1-2")

grafo.adicionaArcoNaoDirigido("V2", "V3", peso=3.5)
grafo.ponderarERotularAresta("V2", "V3", valor_ponderacao=3.5, rotulo="Aresta 2-3")

grafo.adicionaArcoNaoDirigido("V3", "V4", peso=1.2)
grafo.ponderarERotularAresta("V3", "V4", valor_ponderacao=1.2, rotulo="Aresta 3-4")
    # Exportar para GraphML
grafo.exportarParaGraphML("grafo.graphml")