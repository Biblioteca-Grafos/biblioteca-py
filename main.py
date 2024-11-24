from grafo import *
from grafoFuncoes import *
import networkx as nx
import os


def exportarGrafoParaGraphML(grafoNDir, nome_arquivo=r'..\Desktop\Grafo_Trabalho\biblioteca-py\exportar_grafo\grafo.graphml'):
    #COLOCAR O DIRETÓRIO DO COMPUTADOR ESPECÍFICO PARA QUE FUNCIONE
    
    # Garantir que o diretório de destino existe
    diretorio = os.path.dirname(nome_arquivo)
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
    
    G = nx.Graph()  # Para grafo não direcionado
    # G = nx.DiGraph()  # Para grafo direcionado
    
    # Adicionando vértices e arestas ao grafo do NetworkX
    for v1, arestas in grafoNDir.grafo.items():
        G.add_node(v1)
        for v2, peso in arestas:
            G.add_edge(v1, v2, weight=peso)

    # Exportando para o formato GraphML
    nx.write_graphml(G, nome_arquivo)
    print(f"Grafo exportado para {nome_arquivo}")

###Script principal
# print("")
# print("ESSA É A BIBLIOTECA DE MANIPULAÇÃO DE GRAFOS")
# print("")
# grafo = GrafoNaoDirecionado()
# criarGrafoNDirecionado(grafo)
# grafo.mostrarMatrizIncidencia()



####Scripts para testar funcoes

# print("________________________________")
# print("Aqui começa o grafo não direcionado\n")
# grafoNDir = GrafoNaoDirecionado()
# grafoNDir.adicionarVertice("A")
# grafoNDir.adicionarVertice("B")
# grafoNDir.adicionarVertice("C")
# # grafoNDir.checarGrafoVazio()
# grafoNDir.adicionarAresta("A","B", 33)
# grafoNDir.adicionarAresta("B","C", 33)
# grafoNDir.adicionarAresta("A","C", 33)
# grafoNDir.adicionarAresta("A","C", 55)
# grafoNDir.adicionarAresta("C","A", 34)
# grafoNDir.adicionarAresta("C","C", 34)
# grafoNDir.checarGrafoVazio()
# print("Mostrando meu grafo\n")
# grafoNDir.mostrarListaAdjacencia()
# grafoNDir.mostrarMatrizAdjacencia()
# grafoNDir.mostrarMatrizIncidencia()
# grafoNDir.mostrarArestas()
# # print("________________________________");
# print("Verificando adjacência no grafo não direcionado")
# pares_de_vertices = [("A", "B"), ("B", "C"), ("A", "C")]
# for vertice1, vertice2 in pares_de_vertices:
#     grafoNDir.verificarAdjacencia(vertice1, vertice2)
# grafoNDir.verificarAdjacenciaEntreArestas()

# grafoNDir.existeAresta("A","C")
# grafoNDir.existeAresta("A","B")
# grafoNDir.existeAresta("B","A")
# grafoNDir.quantidadeVertices()
# grafoNDir.quantidadeArestas()
# grafoNDir.checarGrafoCompleto()

# Exemplo para criar um grafo direcionado
grafoDir = GrafoDirecionado()
criarGrafoDirecionado(grafoDir)
# grafoDir.adicionarVertice("A")
# grafoDir.adicionarVertice("B")
# grafoDir.adicionarVertice("C")
# grafoDir.checarConectividadeSimples()
grafoDir.checarConectividadeSemifortemente()
# grafoDir.adicionarAresta("A","B", 33)
# grafoDir.adicionarAresta("A", "B", 33) # Não será adicionada novamente
# grafoDir.adicionarAresta("B","C", 33)

# grafoDir.mostrarMatrizAdjacencia()
# grafoDir.mostrarArestas()
# grafoDir.verificarAdjacencia()
# grafoDir.verificarAdjacenciaEntreArestas()
# grafoDir.existeAresta("A","C")
# grafoDir.existeAresta("C","A")
# grafoDir.existeAresta("A","B")
# grafoDir.existeAresta("B","A")
# grafoDir.quantidadeVertices()
# grafoDir.quantidadeArestas()

# print("Aqui começa o grafo direcionado");
# grafoDir = GrafoDirecionado();
# grafoDir.adicionarVertice("Belo Horizonte");
# grafoDir.adicionarVertice("Contagem das Aboboras");
# grafoDir.adicionarAresta("Belo Horizonte", "Contagem das Aboboras");
# grafoDir.adicionarVertice("Betim");
# grafoDir.adicionarAresta("Contagem das Aboboras", "Betim");
# print("Mostrando meu grafo");
# grafoDir.mostrarGrafo();
# print("________________________________");
