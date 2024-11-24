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
            # Atualiza o peso da aresta em ambos os sentidos (para grafos não dirigidos)
            for i, (vizinho, peso) in enumerate(self.grafo[a]):
                if vizinho == b:
                    self.grafo[a][i] = (b, valor_ponderacao)
                    break
            for i, (vizinho, peso) in enumerate(self.grafo[b]):
                if vizinho == a:
                    self.grafo[b][i] = (a, valor_ponderacao)
                    break
        
            # Atualiza o peso também na lista de arestas
            for i, (v1, v2, peso) in enumerate(self.arestas):
                if (v1 == a and v2 == b) or (v1 == b and v2 == a):
                    self.arestas[i] = (a, b, valor_ponderacao)
                    break
        
            # Adiciona o rótulo à aresta
            self.rotulosArestas[(a, b)] = rotulo
            self.rotulosArestas[(b, a)] = rotulo  # Para grafos não dirigidos
            print(f"Aresta ({a}, {b}) ponderada com '{valor_ponderacao}' e rotulada com '{rotulo}'.")
            return True
    
        print(f"Aresta ({a}, {b}) não existe no grafo.")
        return False



    def removeArco(self, a, b):
        if a in self.grafo and b in [v[0] for v in self.grafo[a]]:
            self.grafo[a] = [v for v in self.grafo[a] if v[0] != b]
            print(f"Arco {a} --- {b} removido com sucesso.")
        else:
            print(f"Arco {a} --- {b} não existe e não pode ser removido.")
        
        # Remover também a conexão reversa
        if b in self.grafo and a in [v[0] for v in self.grafo[b]]:
            self.grafo[b] = [v for v in self.grafo[b] if v[0] != a]


    def existeAresta(self, a, b):
        print("Verificando existência entre as arestas:")
        if a in self.grafo and b in self.grafo:  # Verifica se ambos os vértices existem
        # Verifica se b está na lista de adjacência de a
            if any(vizinho == b for vizinho, _ in self.grafo[a]):
                print(f"Existe aresta entre {a} e {b}")
                return True
        print(f"Não existe aresta entre {a} e {b}")
        return False


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
                if vizinho in listaVertices:  # Verifica se o vizinho existe
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

    def ehVazio(self):
        # Um grafo é vazio se não tem vértices ou arestas
        if not self.grafo:  # Sem vértices
            print("O grafo está vazio.")
            return True
        elif not self.arestas:  # Sem arestas
            print("O grafo não tem arestas, mas tem vértices.")
            return True
        print("O grafo não está vazio.")
        return False

    def ehCompleto(self):
        # Um grafo completo deve ter todos os pares de vértices conectados
        n = len(self.grafo)
        if n <= 1:  # Grafo com 0 ou 1 vértice é considerado completo
            print("O grafo é completo.")
            return True

        for vertice, adjacentes in self.grafo.items():
            # Verificar se o número de adjacentes é igual a n-1 (todos os outros vértices)
            if len(adjacentes) != n - 1:
                print("O grafo não é completo.")
                return False

        print("O grafo é completo.")
        return True

    def exportarParaGraphML(self, arquivo):
        import xml.etree.ElementTree as ET

        # Raiz do arquivo GraphML
        graphml = ET.Element("graphml", xmlns="http://graphml.graphdrawing.org/xmlns")
        
        # Definir chaves para atributos de nós e arestas
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
        
        # Definir o grafo
        graph = ET.SubElement(graphml, "graph", id="G", edgedefault="undirected")
        
        # Adicionar vértices
        for vertice in self.grafo:
            node = ET.SubElement(graph, "node", id=vertice)
            
            # Adicionar peso como atributo do nó (se existir)
            if vertice in self.vertices:
                data_weight = ET.SubElement(node, "data", key="weight_node")
                data_weight.text = str(self.vertices[vertice])
            
            # Adicionar rótulo como atributo do nó (se existir)
            if vertice in self.rotulos:
                data_label = ET.SubElement(node, "data", key="label_node")
                data_label.text = self.rotulos[vertice]

        # Adicionar arestas
        for a, b, peso in self.arestas:
            edge = ET.SubElement(graph, "edge", source=a, target=b)
            
            # Adicionar peso como atributo da aresta
            data_weight = ET.SubElement(edge, "data", key="weight_edge")
            data_weight.text = str(peso)
            
            # Adicionar rótulo da aresta, se existir
            if (a, b) in self.rotulosArestas:
                data_label = ET.SubElement(edge, "data", key="label_edge")
                data_label.text = self.rotulosArestas[(a, b)]

        # Converter o XML para string e salvar no arquivo
        tree = ET.ElementTree(graphml)
        tree.write(arquivo, encoding="utf-8", xml_declaration=True)
        print(f"Grafo exportado para {arquivo} no formato GraphML.")
