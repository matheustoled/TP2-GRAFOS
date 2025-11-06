import pandas as pd
import networkx as nx

def CriarMontarGrafo(datasetEscolhido):
    grafo = nx.Graph()

    dados = pd.read_csv("../datasets_coloring/" + datasetEscolhido)

    for i, linha in dados.iterrows():
        disciplina1 = linha["Disciplina1"]
        disciplina2 = linha["Disciplina2"]
        grafo.add_edge(disciplina1, disciplina2)

    return grafo
    
def imprimirDadosGrafo(Grafo):
    print("\n===== DADOS DO GRAFO =====")
    print("Número de vértices:", Grafo.number_of_nodes())
    print("Número de arestas:", Grafo.number_of_edges())
    print("Vértices:", list(Grafo.nodes()))
    print("Arestas:\n", list(Grafo.edges()))
    print("===========================\n")