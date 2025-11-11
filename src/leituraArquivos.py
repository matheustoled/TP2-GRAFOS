from preencherGrafo import *

def lerDataset():
    print("Escolha o dataset que deseja analisar:")
    print("===========================================")
    print("1 - pequeno.csv")
    print("2 - medio.csv")
    print("3 - grande.csv")
    print("4 - teste5.csv")
    print("5 - teste10.csv")
    print("===========================================\n")

    datasetEscolhido = int(input("Digite o numero do arquivo do dataset que deseja analisar: "))

    if(datasetEscolhido == 1):
        datasetEscolhido = "pequeno.csv"
    elif(datasetEscolhido == 2):
        datasetEscolhido = "medio.csv"
    elif(datasetEscolhido == 3):
        datasetEscolhido = "grande.csv"
    elif(datasetEscolhido == 4):
        datasetEscolhido = "teste5.csv"
    elif(datasetEscolhido == 5):
        datasetEscolhido = "teste10.csv"

    grafo = CriarMontarGrafo(datasetEscolhido)

    # imprimirDadosGrafo(grafo)

    return grafo