from grafo import *

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
