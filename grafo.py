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
            print(f"{aresta}")
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

##verificar se é um grafo vazio
    def checarGrafoVazio(self):
        print("\n---------------------------------------------------------------------------------------")
        print("Checando se o grafo é vazio:");
        
        if not self.grafo or all(not arestas for arestas in self.grafo.values()):
            print("O grafo está vazio.")
            return True
        
        print("O grafo não está vazio.")
        return False

 
###########################################################################################################

    def busca_em_profundidade(self, vertice, visitados):
        visitados.add(vertice)
        for v, _ in self.grafo[vertice]:
            if v not in visitados:
                self.busca_em_profundidade(v, visitados)

    def checarConectividadeSimples(self):
        visitados = set()
        
        tem_arestas = any(self.grafo[vertice] for vertice in self.grafo)
        if not tem_arestas:
            print("O grafo possui vértices, mas não possui nenhuma aresta.")
            return False
        
        primeiro_vertice = next(iter(self.grafo))
        self.busca_em_profundidade(primeiro_vertice, visitados)

        if len(visitados) == len(self.grafo):
            print("O grafo é simplesmente conexo!")
            return True
        else:
            print("O grafo não é simplesmente conexo!")
            return False

###########################################################################################################
class GrafoNaoDirecionado(Grafo):
    # def adicionarAresta(self, vertice1, vertice2, peso = 1):
    #     if vertice1 in self.grafo and vertice2 in self.grafo:
    #         self.grafo[vertice1].append((vertice2, peso))
    #         self.grafo[vertice2].append((vertice1, peso))
    #         self.arestas.append((vertice1, vertice2, peso))

    def removerAresta(self, vertice1, vertice2):
        if vertice1 in self.grafo and vertice2 in self.grafo:
            self.grafo[vertice1] = [(v, p) for v, p in self.grafo[vertice1] if v != vertice2]
            self.grafo[vertice2] = [(v, p) for v, p in self.grafo[vertice2] if v != vertice1]
            self.arestas = [(v1, v2, p) for v1, v2, p in self.arestas if (v1, v2) != (vertice1, vertice2) and (v2, v1) != (vertice1, vertice2)]

   # Checagem de adjacência
    def estaoAdjacentes(self, vertice1, vertice2):
        if vertice1 in self.grafo and vertice2 in self.grafo:
            return any(v == vertice2 for v, _ in self.grafo[vertice1])
        return False

    def verificarAdjacencia(self, vertice1, vertice2):
        if self.estaoAdjacentes(vertice1, vertice2):
            print(f"{vertice1} e {vertice2} estão adjacentes.")
        else:
            print(f"{vertice1} e {vertice2} NÃO estão adjacentes.")


    def verificarAdjacenciaEntreArestas(self):
        """Verifica a adjacência entre todas as arestas do grafo."""
        print("Verificando adjacência entre as arestas:")
        for i in range(len(self.arestas)):
            v1_1, v1_2, peso1 = self.arestas[i]
            for j in range(i + 1, len(self.arestas)):  # Evitar comparações duplicadas
                v2_1, v2_2, peso2 = self.arestas[j]
                
                # Verifica se as arestas compartilham pelo menos um vértice
                if (v1_1 == v2_1 or v1_1 == v2_2 or 
                    v1_2 == v2_1 or v1_2 == v2_2):
                    print(
                        f"Aresta ({v1_1} - {v1_2}, peso {peso1}) "
                        f"está adjacente à aresta ({v2_1} - {v2_2}, peso {peso2})."
                    )
                else:
                    print(
                        f"Aresta ({v1_1} - {v1_2}, peso {peso1}) "
                        f"NÃO está adjacente à aresta ({v2_1} - {v2_2}, peso {peso2})."
                    )

                    ###########################################################################################################
###########################################################################################################

    def adicionarAresta(self, origem, destino, peso = 1):
        if origem == destino:
            print(f"Não é permitido adicionar uma aresta de {origem} para {destino} (laço).")
            return
    
        # Verifica automaticamente se a aresta já existe
        if self.existeAresta(origem, destino):
            print(f"Aresta de {origem} para {destino} já existe! Ação ignorada.")
            # Atualiza pesos caso sejam diferentes do que foi informado anteriormente, atualizando os vértices e suas relações e também a lista de arestas
            for idx, (v, p) in enumerate(self.grafo[origem]):
                if v == destino:
                    if p != peso :
                        self.grafo[origem][idx] = (destino, peso)
                        print(f"Peso da aresta de {origem} para {destino} atualizado para {peso}.")

            for idx, (v, p) in enumerate(self.grafo[destino]):
                if v == origem:
                    if p != peso :
                        self.grafo[destino][idx] = (origem, peso)
                        print(f"Peso da aresta de {destino} para {origem} atualizado para {peso}.")

            for idx, (a, b, p) in enumerate(self.arestas):
                if (a == origem and b == destino) or (a == destino and b == origem):
                    if p != peso:
                        self.arestas[idx] = (a, b, peso)
                        print(f"Peso da aresta na lista de arestas atualizado para {peso}.")
            return

        if origem in self.grafo and destino in self.grafo:
            self.grafo[origem].append((destino, peso))
            self.grafo[destino].append((origem, peso))
            self.arestas.append((origem, destino, peso))
            print(f"Aresta não direcionada adicionada de {origem} para {destino} com peso {peso}.")

    def existeAresta(self, origem, destino):
        """Verifica se existe uma aresta de origem para destino."""
        print("\n---------------------------------------------------------------------------------------")
        print("Verificando existencia entre as arestas:")

        if origem in self.grafo and destino in self.grafo:
            for v, _ in self.grafo[origem]:
                if v == destino:
                    print(f"Existe aresta entre {origem} para {destino}")
                    return True
                
            for v, _ in self.grafo[destino]:
                if v == origem:
                    print(f"Existe aresta entre {origem} para {destino}")
                    return True
        return print(f"Não existe aresta entre {origem} para {destino}")

###########################################################################################################
###########################################################################################################

    def quantidadeVertices(self):
        print("\n---------------------------------------------------------------------------------------")
        """Retorna a quantidade de vértices no grafo."""
        print(f"A quantidade de vértices no grafo é de: {len(self.grafo)}")
        # return len(self.grafo)

    def quantidadeArestas(self):
        print("\n---------------------------------------------------------------------------------------")
        """Retorna a quantidade de arestas no grafo."""
        print(f"A quantidade de arestas no grafo é de: {len(self.arestas)}")
        # return len(self.arestas)

 ###########################################################################################################

    def checarGrafoCompleto(self):
        print("\n---------------------------------------------------------------------------------------")
        print("Checagem se o grafo é completo:");
        numero_vertices = len(self.grafo)
        numero_arestas = len(self.arestas)

        numero_maximo_arestas = numero_vertices * (numero_vertices - 1) // 2

        if numero_arestas == numero_maximo_arestas:
            print("O grafo é completo!")
            return True
        else:
            print("O grafo não é completo.")
            return False

###########################################################################################################           
class GrafoDirecionado(Grafo):
    def adicionarAresta(self, origem, destino, peso=1):
        if origem in self.grafo and destino in self.grafo:
            self.grafo[origem].append((destino, peso))  # Corrigido: passando tupla (destino, peso)
            self.arestas.append((origem, destino, peso))

    def removerAresta(self, origem, destino):
        if origem in self.grafo and destino in self.grafo:
            self.grafo[origem] = [(v, p) for v, p in self.grafo[origem] if v != destino]


   
    def estaoAdjacentes(self, vertice1, vertice2):
        if vertice1 in self.grafo and vertice2 in self.grafo:
            return any(v == vertice2 for v, _ in self.grafo[vertice1])
        return False
    
    
  
    def verificarAdjacencia(self):
        vertices = list(self.grafo.keys())
        print("\n---------------------------------------------------------------------------------------")
        print("Verificando adjacência entre os vértices no grafo direcionado:")
        for i in range(len(vertices)):
            for j in range(len(vertices)):
                if i != j:  # Não verificar a adjacência de um vértice consigo mesmo
                    vertice1 = vertices[i]
                    vertice2 = vertices[j]
                    if self.estaoAdjacentes(vertice1, vertice2):
                        print(f"{vertice1} e {vertice2} estão adjacentes.")
                    else:
                        print(f"{vertice1} e {vertice2} NÃO estão adjacentes.")
      


    def estaoAdjacentesArestas(self, aresta1, aresta2):
        """Verifica se duas arestas estão adjacentes."""
        origem1, destino1, _ = aresta1
        origem2, destino2, _ = aresta2

        # A aresta1 é adjacente à aresta2 se o destino da primeira for a origem da segunda
        return destino1 == origem2

    def verificarAdjacenciaEntreArestas(self):
        """Verifica a adjacência entre todas as arestas do grafo."""
        print("\n---------------------------------------------------------------------------------------")
        print("Verificando adjacência entre as arestas:")
        for i in range(len(self.arestas)):
            for j in range(i + 1, len(self.arestas)):
                aresta1 = self.arestas[i]
                aresta2 = self.arestas[j]

                if self.estaoAdjacentesArestas(aresta1, aresta2):
                    print(f"Aresta {aresta1} está adjacente à aresta {aresta2}.")
                else:
                    print(f"Aresta {aresta1} NÃO está adjacente à aresta {aresta2}.")
                   
###########################################################################################################
###########################################################################################################

    def adicionarAresta(self, origem, destino, peso=1):
        # Verifica automaticamente se a aresta já existe
        if self.existeAresta(origem, destino):
            print(f"Aresta de {origem} para {destino} já existe! Ação ignorada.")
            return

        if origem in self.grafo and destino in self.grafo:
            self.grafo[origem].append((destino, peso))
            self.arestas.append((origem, destino, peso))
            print(f"Aresta direcionada adicionada de {origem} para {destino} com peso {peso}.")

    def existeAresta(self, origem, destino):
        """Verifica se existe uma aresta de origem para destino."""
        print("\n---------------------------------------------------------------------------------------")
        print("Verificando existencia entre as arestas:")

        if origem in self.grafo and destino in self.grafo:
            for v, _ in self.grafo[origem]:
                if v == destino:
                    return print(f"Existe aresta entre {origem} para {destino}")
                
        if destino in self.grafo and origem in self.grafo:
            for v, _ in self.grafo[destino]:
                if v == origem:
                    return print(f"Existe aresta entre {origem} para {destino}")
        return print(f"Não existe aresta entre {origem} para {destino}")

###########################################################################################################
###########################################################################################################

    def quantidadeVertices(self):
        print("\n---------------------------------------------------------------------------------------")
        """Retorna a quantidade de vértices no grafo."""
        print(f"A quantidade de vértices no grafo é de: {len(self.grafo)}")
        # return len(self.grafo)

    def quantidadeArestas(self):
        print("\n---------------------------------------------------------------------------------------")
        """Retorna a quantidade de arestas no grafo."""
        print(f"A quantidade de arestas no grafo é de: {len(self.arestas)}")
        # return len(self.arestas)

###########################################################################################################

    def checarGrafoCompleto(self):
        print("\n---------------------------------------------------------------------------------------")
        print("Checagem se o grafo é completo:");
        numero_vertices = len(self.grafo)
        numero_arestas = len(self.arestas)

        numero_maximo_arestas = numero_vertices * (numero_vertices - 1)
        print(numero_arestas)
        print(numero_maximo_arestas)

        if numero_arestas == numero_maximo_arestas:
            print("O grafo é completo!")
            return True
        else:
            print("O grafo não é completo.")
            return False
###########################################################################################################
    
    def busca_em_profundidade(self, vertice, visitados, componente = None):
        visitados.add(vertice)
        if componente is not None:
            componente.append(vertice)
        
        for v, _ in self.grafo[vertice]:
            if v not in visitados:
                self.busca_em_profundidade(v, visitados, componente)
    
    def checarConectividadeSimples(self):
        for vertice in self.grafo:
            for vizinho, peso in self.grafo[vertice]:
                if not any(v == vertice for v, _ in self.grafo[vizinho]):
                    self.grafo[vizinho].append((vertice, peso))
        
        visitados = set()
        
        tem_arestas = any(self.grafo[vertice] for vertice in self.grafo)
        if not tem_arestas:
            print("O grafo possui vértices, mas não possui nenhuma aresta. Logo, não é simplesmente conexo.")
            return False
        
        primeiro_vertice = next(iter(self.grafo))
        self.busca_em_profundidade(primeiro_vertice, visitados)

        if len(visitados) == len(self.grafo):
            print("O grafo é simplesmente conexo!")
            return True
        else:
            print("O grafo não é simplesmente conexo!")
            return False

###########################################################################################################
    def criarGrafoReverso(self):
        grafo_reverso = GrafoDirecionado()
        for vertice in self.grafo:
            grafo_reverso.adicionarVertice(vertice)
            print(f"Vértice {vertice} adicionado ao grafo reverso.")
        
        for vertice in self.grafo:
            for vizinho, peso in self.grafo[vertice]:
                print(f"Adicionando aresta de {vizinho} para {vertice} com peso {peso}")
                grafo_reverso.adicionarAresta(vizinho, vertice, peso)

        return grafo_reverso


    def checarConectividadeSemifortemente(self):
        grafo_reverso = self.criarGrafoReverso()

        for vertice in self.grafo:
            visitados_normal = set()
            self.busca_em_profundidade(vertice, visitados_normal)
            
            visitados_reverso = set()
            grafo_reverso.busca_em_profundidade(vertice, visitados_reverso)
            
            if len(visitados_normal) != len(self.grafo) or len(visitados_reverso) != len(self.grafo):
                print(f"O grafo não é semifortemente conexo!")
                return False

        print("O grafo é semifortemente conexo!")
        return True
    
    def checarConectividadeFortemente(self):
        visitados_original = set()
        primeiro_vertice = next(iter(self.grafo))  # Pega o primeiro vértice
        self.busca_em_profundidade(primeiro_vertice, visitados_original)

        if len(visitados_original) != len(self.grafo):
            print("O grafo não é fortemente conexo!")
            return False

        grafo_reverso = self.criarGrafoReverso()

        visitados_reverso = set()
        grafo_reverso.busca_em_profundidade(primeiro_vertice, visitados_reverso)

        if len(visitados_reverso) == len(self.grafo):
            print("O grafo é fortemente conexo!")
            return True
        else:
            print("O grafo não é fortemente conexo!")
            return False
        
    def kosaraju(self):
        from collections import deque
        stack = deque()
        visitados = set()
        
        for vertice in self.grafo:
            if vertice not in visitados:
                self._dfs_ordenar(vertice, visitados, stack)

        grafo_reverso = self.criarGrafoReverso()
        
        visitados.clear()
        componentes = []

        while stack:
            vertice = stack.pop()
            if vertice not in visitados:
                componente = []
                grafo_reverso.busca_em_profundidade(vertice, visitados, componente)
                componentes.append(componente)
        
        print("Componentes fortemente conexos:", componentes)
        return componentes

    def _dfs_ordenar(self, vertice, visitados, stack):
        visitados.add(vertice)
        for v, _ in self.grafo[vertice]:
            if v not in visitados:
                self._dfs_ordenar(v, visitados, stack)
        stack.append(vertice)