from datetime import datetime
import random
start = datetime.now()
# Definição dos parâmetros do problema
capacidade_mochila = 50

itens = []

for i in range(1, 100):
    nome = "Item" + str(i)
    valor = random.randint(1, 100)
    peso = random.randint(1, 50)
    item = (nome, valor, peso)
    itens.append(item)

# Função para resolver o problema da mochila usando programação dinâmica
def resolver_mochila():
    num_itens = len(itens)

    # Criação de uma tabela de programação dinâmica
    tabela = [[0] * (capacidade_mochila + 1) for _ in range(num_itens + 1)]

    # Preenchimento da tabela
    for i in range(1, num_itens + 1):
        nome, valor, peso = itens[i - 1]
        for j in range(1, capacidade_mochila + 1):
            if peso > j:
                tabela[i][j] = tabela[i - 1][j]
            else:
                tabela[i][j] = max(tabela[i - 1][j], tabela[i - 1][j - peso] + valor)

    # Reconstrução da solução
    solucao = []
    i = num_itens
    j = capacidade_mochila
    while i > 0 and j > 0:
        if tabela[i][j] != tabela[i - 1][j]:
            nome, valor, peso = itens[i - 1]
            solucao.append(nome)
            i -= 1
            j -= peso
        else:
            i -= 1

    return solucao, tabela[num_itens][capacidade_mochila]

# Resolvendo o problema da mochila usando programação dinâmica
melhor_comb, melhor_valor = resolver_mochila()

end = datetime.now()
#execution_time = end_time - start_time
# Exibindo o resultado
print("Melhor combinação de itens:", melhor_comb)
print("Valor total:", melhor_valor)
print("Tempo de execução: ", str(end - start)[5:])

