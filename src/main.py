import pandas as pd
import gcol
import matplotlib.pyplot as mp
import time

from leituraArquivos import *

G_nx = lerDataset()

inicio = time.time()
# convertendo o grafo do NetworkX para o formato do gcol e colorindo seus vertices
G_gcol_colorido = gcol.node_coloring(G_nx)
fim = time.time()

tempo_execucao = fim - inicio

cores = gcol.get_node_colors(G_nx, G_gcol_colorido)
pos1 = nx.spring_layout(G_nx, seed=1)
pos2 = gcol.coloring_layout(G_nx, G_gcol_colorido)
pos3 = gcol.multipartite_layout(G_nx, G_gcol_colorido)

print("\n===== RESULTADOS =====")
print("Numero minimo de cores utilizadas (Horarios) =", max(G_gcol_colorido.values()) + 1)
print("Cor atribuida a cada disciplina:")
for disciplina, cor in G_gcol_colorido.items():
    if cor == 0:
        cor = "Azul Escuro"
    elif cor == 1:
        cor = "Azul Claro"
    elif cor == 2:
        cor = "Laranja"
    print(f"  {disciplina}: {cor}")
print(f"Tempo de execucao aproximado: {tempo_execucao:.6f} segundos")
print("======================\n")

nx.draw_networkx(G_nx,
                 pos=pos1,
                 node_color=cores)
mp.show()

nx.draw_networkx(G_nx,
                 pos=pos2,
                 node_color=cores)
mp.show()

nx.draw_networkx(G_nx,
                 pos=pos3,
                 node_color=cores)
mp.show()
