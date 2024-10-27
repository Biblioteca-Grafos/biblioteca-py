from grafo import *
from grafoFuncoes import *


###Script principal
# print("")
# print("ESSA É A BIBLIOTECA DE MANIPULAÇÃO DE GRAFOS")
# print("")
# grafo = GrafoNaoDirecionado()
# criarGrafoNDirecionado(grafo)
# grafo.mostrarMatrizIncidencia()



####Scripts para testar funcoes

print("________________________________");
print("Aqui começa o grafo não direcionado\n");
grafoNDir = GrafoNaoDirecionado();
grafoNDir.adicionarVertice("A");
grafoNDir.adicionarVertice("B");
grafoNDir.adicionarVertice("C");
grafoNDir.adicionarAresta("A","B", 33);
grafoNDir.adicionarAresta("B","C", 33);
print("Mostrando meu grafo\n");
grafoNDir.mostrarListaAdjacencia();
grafoNDir.mostrarMatrizAdjacencia();
grafoNDir.mostrarMatrizIncidencia();
grafoNDir.mostrarArestas();
# print("________________________________");
print("Verificando adjacência no grafo não direcionado")
pares_de_vertices = [("A", "B"), ("B", "C"), ("A", "C")]
for vertice1, vertice2 in pares_de_vertices:
    grafoNDir.verificarAdjacencia(vertice1, vertice2)
grafoNDir.verificarAdjacenciaEntreArestas()


# Exemplo para criar um grafo direcionado
grafoDir = GrafoDirecionado()
criarGrafoDirecionado(grafoDir)
grafoDir.mostrarMatrizAdjacencia()
grafoDir.mostrarArestas()
grafoDir.verificarAdjacencia()
grafoDir.verificarAdjacenciaEntreArestas()


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
