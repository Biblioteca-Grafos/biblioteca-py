import random
import xml.etree.ElementTree as ET

class Grafo:
    def __init__(self):
        self.grafo = {}
        self.arestas = []
        self.vertices = {}
        self.rotulos = {}
        self.rotulosArestas = {}

##Criar adicionar excluir etc
    def criarGrafo(self,x):
        for i in range(x):
            vertice = f"V{i+1}"
            self.adicionarVertice(vertice)

    def criarGrafoAleatorio(self, minVertices, maxVertices, minArcos, maxArcos):
        vertices = random.randint(minVertices, maxVertices)
        maxArcoPossivel = vertices * (vertices - 1) // 2
        num_arestas = random.randint(minArcos, min(maxArcos, maxArcoPossivel))

        print(f"Gerando grafo com {vertices} vértices e {num_arestas} arestas.")
        
        self.criarGrafo(vertices)
        
        # Obter lista de vértices
        verticess = list(self.grafo.keys())
        
        # Adicionar arestas aleatórias
        arestas_criadas = 0
        while arestas_criadas < num_arestas:
            a, b = random.sample(verticess, 2)  # Selecionar dois vértices diferentes aleatoriamente
            if self.adicionaArcoNaoDirigido(a, b):
                arestas_criadas += 1

    def criarGrafoReverso(self):
        grafo_reverso = Grafo()


        for vertice in self.grafo:
            grafo_reverso.adicionarVertice(vertice)
            
            if vertice in self.vertices:
                grafo_reverso.ponderarERotularVertice(vertice, self.vertices[vertice], self.rotulos.get(vertice, ""))
            print(f"Vértice {vertice} adicionado ao grafo reverso.")


        for vertice in self.grafo:
            for vizinho, peso in self.grafo[vertice]:

                print(f"Adicionando aresta reversa de {vizinho} para {vertice} com peso {peso}")
                grafo_reverso.adicionaArcoDirigido(vizinho, vertice)
                grafo_reverso.ponderarERotularAresta(vizinho, vertice, peso, self.rotulosArestas.get((vertice, vizinho), ""))
        
        return grafo_reverso

    def adicionarVertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []
            return True
        return False

    def adicionaArcoNaoDirigido(self, a, b, peso=1):
        if a in self.grafo and b in self.grafo and b not in [v for v, _ in self.grafo[a]]:
            self.grafo[a].append((b, peso))
            self.grafo[b].append((a, peso))
            self.arestas.append((a, b, peso))
            print(f"Arco {a} --- {b} adicionado com peso {peso}")
            return True
        print("Falha ao adicionar arco")
        return False

    def adicionaArcoDirigido(self, a, b):
        if a in self.grafo and b in self.grafo:
            self.grafo[a].append(b)
            print(f"Arco de {a} ---> {b} adicionado")
            return True
        print("falha ao adicionar Arco")
        return False

    def ponderarERotularVertice(self, v, valor_ponderacao, rotulo):
        if v in self.grafo:
            self.vertices[v] = valor_ponderacao  # Ponderação do vértice
            self.rotulos[v] = rotulo  # Rótulo do vértice
            print(f"Vértice '{v}' ponderado com '{valor_ponderacao}' e rotulado com '{rotulo}'.")
            return True
        print(f"Vértice '{v}' não existe no grafo.")
        return False

    def ponderarERotularAresta(self, a, b, valor_ponderacao, rotulo):
        if a in self.grafo and b in self.grafo:
            for i, (vizinho, peso) in enumerate(self.grafo[a]):
                if vizinho == b:
                    self.grafo[a][i] = (b, valor_ponderacao)
                    break
            for i, (vizinho, peso) in enumerate(self.grafo[b]):
                if vizinho == a:
                    self.grafo[b][i] = (a, valor_ponderacao)
                    break
        
            for i, (v1, v2, peso) in enumerate(self.arestas):
                if (v1 == a and v2 == b) or (v1 == b and v2 == a):
                    self.arestas[i] = (a, b, valor_ponderacao)
                    break
        

            self.rotulosArestas[(a, b)] = rotulo
            self.rotulosArestas[(b, a)] = rotulo
            print(f"Aresta ({a}, {b}) ponderada com '{valor_ponderacao}' e rotulada com '{rotulo}'.")
            return True
    
        print(f"Aresta ({a}, {b}) não existe no grafo.")
        return False

    def removeArco(self, a, b):
        if a in self.grafo:
            if b in [v[0] for v in self.grafo[a]]:
                self.grafo[a] = [v for v in self.grafo[a] if v[0] != b]
                print(f"Arco {a} --- {b} removido com sucesso.")
        else:
            print(f"Arco {a} --- {b} não existe e não pode ser removido.")
        
        if b in self.grafo and a in [v[0] for v in self.grafo[b]]:
            self.grafo[b] = [v for v in self.grafo[b] if v[0] != a]

##funcoes para exibir o grafo##
    def mostrarVertices(self):
        print("Mostrando todos os vertices do Grafo")
        for vertice in self.grafo:
            print(f"{vertice}")
        print("Fim mostrando todos os vertices do Grafo\n")

    def mostrarListaAdjacencia(self):
        print("Representando Grafo com Lista de Adjacência")
        for vertice, adjacentes in self.grafo.items():
            adjacencias = [f"{vizinho}({peso})" for vizinho, peso in adjacentes]
            print(f"{vertice} -> {' '.join(adjacencias)}")
        print("Fim representando Grafo com Lista de Adjacência\n")

    def mostrarMatrizAdjacencia(self):
        listaVertices = list(self.grafo.keys())
        quantVertices = len(listaVertices)
        minhaMatriz = [[0] * quantVertices for _ in range(quantVertices)]

        for i, vertice1 in enumerate(listaVertices):
            for vizinho, peso in self.grafo[vertice1]:
                if vizinho in listaVertices:
                    j = listaVertices.index(vizinho)
                    minhaMatriz[i][j] = peso

        print("Representando Grafo com Matriz de Adjacência")
        print("  ", " ".join(listaVertices))
        for i in range(quantVertices):
            linha = [str(minhaMatriz[i][j]) for j in range(quantVertices)]
            print(f"{listaVertices[i]} " + " ".join(linha))
        print("Fim representando Grafo com Matriz de Adjacência\n")

    def mostrarMatrizIncidencia(self):
        listaVertices = list(self.grafo.keys())
        quantVertices = len(listaVertices)
        quantArestas = len(self.arestas)
        minhaMatriz = [[0] * quantArestas for _ in range(quantVertices)]

        for i, (vertice1, vertice2, peso) in enumerate(self.arestas):
            j = listaVertices.index(vertice1)
            k = listaVertices.index(vertice2)
            minhaMatriz[j][i] = 1
            minhaMatriz[k][i] = 1

        print("Representando Grafo com Matriz de Incidência")
        print("  ", " ".join(f"E{index+1}" for index in range(quantArestas)))
        for i in range(quantVertices):
            linha = [str(minhaMatriz[i][j]) for j in range(quantArestas)]
            print(f"{listaVertices[i]} " + " ".join(linha))
        print("Fim representando Grafo com Matriz de Incidência\n")


####Verificaçoes

    def existeAresta(self, a, b):
        print("Verificando existência entre as arestas:")
        if a in self.grafo and b in self.grafo: 
            if any(vizinho == b for vizinho, _ in self.grafo[a]):
                print(f"Existe aresta entre {a} e {b}")
                return True
        print(f"Não existe aresta entre {a} e {b}")
        return False

    def ehVazio(self):

        if not self.grafo:  # Sem vértices
            print("O grafo está vazio.")
            return True
        elif not self.arestas:  # Sem arestas
            print("O grafo não tem arestas, mas tem vértices.")
            return True
        print("O grafo não está vazio.")
        return False

    def ehCompleto(self):
        n = len(self.grafo)
        if n <= 1:  # Grafo com 0 ou 1 vértice é considerado completo
            print("O grafo é completo.")
            return True

        for vertice, adjacentes in self.grafo.items():
            if len(adjacentes) != n - 1:
                print("O grafo não é completo.")
                return False

        print("O grafo é completo.")
        return True

########Verificar Conectividade
    def busca_em_profundidade(self, vertice, visitados):
        visitados.add(vertice)
        for v, _ in self.grafo.get(vertice, []):
            if v not in visitados:
                self.busca_em_profundidade(v, visitados)

    def checarConectividadeSimples(self):
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

    def checarConectividadeSemifortemente(self):
        grafo_reverso = self.criarGrafoReverso()

        for vertice in self.grafo:
            visitados_normal = set()
            self.busca_em_profundidade(vertice, visitados_normal)
            
            visitados_reverso = set()
            grafo_reverso.busca_em_profundidade(vertice, visitados_reverso)
            
            if len(visitados_normal) != len(self.grafo) or len(visitados_reverso) != len(self.grafo):
                print("O grafo não é semifortemente conexo!")
                return False

        print("O grafo é semifortemente conexo!")
        return True

    def checarConectividadeFortemente(self):
        visitados_original = set()
        primeiro_vertice = next(iter(self.grafo))  # Pega o primeiro vértice
        self.busca_em_profundidade(primeiro_vertice, visitados_original)

        if len(visitados_original) != len(self.grafo):
            print("O grafo não é fortemente conexo! (não todos os vértices são acessíveis a partir de um vértice)")
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



####Exportaçao
    def exportarParaGraphML(self, arquivo):
        import xml.etree.ElementTree as ET

        # Raiz do arquivo GraphML
        graphml = ET.Element("graphml", xmlns="http://graphml.graphdrawing.org/xmlns")
        
        #chaves para atributos de nós e arestas
        keys = [
            {"id": "weight_node", "for": "node", "attr.name": "weight", "attr.type": "double"},
            {"id": "label_node", "for": "node", "attr.name": "label", "attr.type": "string"},
            {"id": "weight_edge", "for": "edge", "attr.name": "weight", "attr.type": "double"},
            {"id": "label_edge", "for": "edge", "attr.name": "label", "attr.type": "string"},
        ]
        
        # Adicionar chaves no arquivo GraphML
        for key in keys:
            ET.SubElement(graphml, "key", id=key["id"], for_=key["for"], 
                        attr_name=key["attr.name"], attr_type=key["attr.type"])
        
        graph = ET.SubElement(graphml, "graph", id="G", edgedefault="undirected")
        

        for vertice in self.grafo:
            node = ET.SubElement(graph, "node", id=vertice)
            
            if vertice in self.vertices:
                data_weight = ET.SubElement(node, "data", key="weight_node")
                data_weight.text = str(self.vertices[vertice])
            
            if vertice in self.rotulos:
                data_label = ET.SubElement(node, "data", key="label_node")
                data_label.text = self.rotulos[vertice]
        
        for (a, b, peso) in self.arestas:
            edge = ET.SubElement(graph, "edge", source=a, target=b)
            
            if (a, b) in self.rotulosArestas:
                data_label = ET.SubElement(edge, "data", key="label_edge")
                data_label.text = self.rotulosArestas[(a, b)]
            
            data_weight = ET.SubElement(edge, "data", key="weight_edge")
            data_weight.text = str(peso)
        
        tree = ET.ElementTree(graphml)
        tree.write(arquivo)
        print(f"Grafo exportado para {arquivo}")
