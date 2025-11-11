import gcol
import matplotlib.pyplot as mp
import time
from leituraArquivos import *

G_nx = lerDataset()

print("\nEscolha o algoritmo de coloração que deseja usar:")
print("===========================================")
print("1 - DSATUR (boa qualidade, mais comum)")
print("2 - Welsh-Powell (rápido)")
print("3 - Random (aleatório)")
print("4 - RLF (Recursive Largest First)")
print("===========================================\n")

opcao = int(input("Digite o número do algoritmo desejado: "))

if opcao == 1:
    estrategia = "dsatur"
elif opcao == 2:
    estrategia = "welsh_powell"
elif opcao == 3:
    estrategia = "random"
elif opcao == 4:
    estrategia = "rlf"
else:
    print("Opção inválida, usando DSATUR por padrão.")
    estrategia = "dsatur"

inicio = time.time()
G_gcol_colorido = gcol.node_coloring(G_nx, strategy=estrategia)
fim = time.time()

tempo_execucao = fim - inicio

cores = gcol.get_node_colors(G_nx, G_gcol_colorido)
pos1 = nx.spring_layout(G_nx, seed=1)
pos2 = gcol.coloring_layout(G_nx, G_gcol_colorido)
pos3 = gcol.multipartite_layout(G_nx, G_gcol_colorido)

print("\n===== RESULTADOS =====")
print(f"Algoritmo utilizado: {estrategia.upper()}")
print("Número mínimo de cores utilizadas (Horários):", max(G_gcol_colorido.values()) + 1)
print("Cor atribuída a cada disciplina:")

for disciplina, cor in G_gcol_colorido.items():
    if cor == 0:
        cor_nome = "Azul Escuro"
    elif cor == 1:
        cor_nome = "Azul Claro"
    elif cor == 2:
        cor_nome = "Laranja Escuro"
    elif cor == 3:
        cor_nome = "Laranja Claro"
    elif cor == 4:
        cor_nome = "Verde Escuro"
    elif cor == 5:
        cor_nome = "Verde Claro"
    elif cor == 6:
        cor_nome = "Vermelho"
    elif cor == 7:
        cor_nome = "Salmao"
    elif cor == 8:
        cor_nome = "Roxo Escuro"
    elif cor == 9:
        cor_nome = "Roxo Claro"
    else:
        cor_nome = f"Cor {cor}"
    print(f"  {disciplina}: {cor_nome}")

print(f"Tempo de execução aproximado: {tempo_execucao:.6f} segundos")
print("======================\n")

nx.draw_networkx(G_nx, pos=pos1, node_color=cores, with_labels=True, cmap=mp.cm.Set3)
mp.title(f"Coloração - Layout Spring ({estrategia.upper()})")
mp.show()

nx.draw_networkx(G_nx, pos=pos2, node_color=cores, with_labels=True, cmap=mp.cm.Set3)
mp.title(f"Coloração - Layout por Cor ({estrategia.upper()})")
mp.show()

nx.draw_networkx(G_nx, pos=pos3, node_color=cores, with_labels=True, cmap=mp.cm.Set3)
mp.title(f"Coloração - Layout Multipartite ({estrategia.upper()})")
mp.show()
