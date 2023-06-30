import random
from datetime import datetime
# Definição dos parâmetros do problema
start = datetime.now()
capacidade_mochila = 100
itens = []

for i in range(1, 100):
    nome = "Item" + str(i)
    valor = random.randint(1, 100)
    peso = random.randint(1, 50)
    item = (nome, valor, peso)
    itens.append(item)

# Parâmetros do algoritmo genético
tamanho_populacao = 10
taxa_mutacao = 0.1
numero_geracoes = 50

def criar_individuo():
    # Função para criar um indivíduo (cromossomo) aleatoriamente
    return [random.randint(0, 1) for _ in range(len(itens))]

def criar_populacao():
    # Função para criar uma população inicial de indivíduos
    return [criar_individuo() for _ in range(tamanho_populacao)]

def avaliar_fitness(individuo):
    # Função para avaliar o fitness (aptidão) de um indivíduo
    valor_total = 0
    peso_total = 0
    for i, item in enumerate(itens):
        if individuo[i] == 1:
            valor_total += item[1]
            peso_total += item[2]
    if peso_total > capacidade_mochila:
        valor_total = 0  # Penaliza soluções inválidas
    return valor_total


def selecionar_pais(populacao):
    # Função para selecionar os pais para reprodução
    pais = []
    for _ in range(2):
        pais.append(random.choice(populacao))
    return pais

def cruzar(pai1, pai2):
    # Função para realizar o cruzamento (recombinação) entre dois pais
    ponto_corte = random.randint(1, len(pai1) - 1)
    filho = pai1[:ponto_corte] + pai2[ponto_corte:]
    return filho

def mutar(individuo):
    # Função para aplicar mutação em um indivíduo
    for i in range(len(individuo)):
        if random.random() < taxa_mutacao:
            individuo[i] = 1 - individuo[i]
    return individuo

def gerar_descendentes(populacao):
    # Função para gerar os descendentes da próxima geração
    descendentes = []
    while len(descendentes) < tamanho_populacao:
        pai1, pai2 = selecionar_pais(populacao)
        filho = cruzar(pai1, pai2)
        filho = mutar(filho)
        descendentes.append(filho)
    return descendentes

def encontrar_melhor_solucao():
    # Função principal para encontrar a melhor solução usando o algoritmo genético
    populacao = criar_populacao()
    melhor_fitness = 0
    melhor_individuo = None

    for _ in range(numero_geracoes):
        fitness_populacao = []
        for individuo in populacao:
            fitness = avaliar_fitness(individuo)
            fitness_populacao.append((individuo, fitness))

            if fitness > melhor_fitness:
                melhor_fitness = fitness
                melhor_individuo = individuo

        fitness_populacao.sort(key=lambda x: x[1], reverse=True)
        selecionados = [individuo for individuo, _ in fitness_populacao[:tamanho_populacao]]
        descendentes = gerar_descendentes(selecionados)
        populacao = selecionados + descendentes[:tamanho_populacao - len(selecionados)]

    return melhor_individuo, melhor_fitness



melhor_individuo, melhor_fitness = encontrar_melhor_solucao()
end = datetime.now()
# Exibir resultados
print("Melhor indivíduo:", melhor_individuo)
print("Valor total:", melhor_fitness)
print("Tempo de execução: ", str(end - start)[5:])