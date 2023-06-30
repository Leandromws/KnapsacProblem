# Análise de Algoritmos para o Problema da Mochila

Neste projeto, realizamos uma análise comparativa entre dois algoritmos diferentes para resolver o clássico problema da mochila: Algoritmo Genético e Programação Dinâmica. Medimos o tempo de execução de ambos os algoritmos para diferentes tamanhos de entrada, variando de 100 a 100.000 itens, a fim de determinar qual abordagem é mais eficiente em termos de tempo.

## Descrição do Problema da Mochila

O problema da mochila é um problema de otimização combinatória em que se busca encontrar a melhor combinação de itens para colocar em uma mochila, maximizando o valor total desses itens, respeitando a capacidade máxima da mochila.

## Algoritmo Genético

O algoritmo genético é uma técnica de otimização inspirada no processo de evolução biológica. Neste contexto, o problema da mochila é abordado da seguinte maneira:

1. **Inicialização**: Gera-se uma população inicial de indivíduos (soluções candidatas) aleatórias.
2. **Avaliação**: Cada indivíduo é avaliado de acordo com seu valor total e sua adequação às restrições da capacidade da mochila.
3. **Seleção**: Com base nas avaliações, os indivíduos mais aptos são selecionados para reprodução.
4. **Reprodução**: Os indivíduos selecionados são combinados por meio de operadores genéticos, como cruzamento e mutação, para gerar novos indivíduos.
5. **Substituição**: A nova geração substitui a anterior.
6. **Critério de parada**: O processo é repetido até atingir um critério de parada, como um número máximo de iterações ou um valor de adequação desejado.

O algoritmo genético é conhecido por sua capacidade de encontrar soluções aproximadas para problemas de otimização combinatória em um tempo razoável. No entanto, sua eficiência depende da natureza do problema e do tamanho da entrada.

## Programação Dinâmica

A programação dinâmica é uma técnica que resolve problemas dividindo-os em subproblemas menores e, em seguida, combinando as soluções desses subproblemas para obter a solução global. Para o problema da mochila, a abordagem de programação dinâmica é a seguinte:

1. **Definição da Tabela**: Cria-se uma tabela de tamanho (número de itens) x (capacidade máxima da mochila), onde cada célula representa a solução ótima para um subproblema.
2. **Preenchimento da Tabela**: Para cada item e capacidade, calcula-se o valor máximo que pode ser alcançado considerando os itens anteriores e a capacidade restante.
3. **Recuperação da Solução**: A partir da tabela preenchida, é possível recuperar a combinação de itens que compõem a solução ótima.

A programação dinâmica é uma abordagem determinística que garante a obtenção da solução ótima para o problema da mochila. No entanto, sua eficiência depende do tamanho da entrada e da complexidade da função objetivo.

## Resultados de Tempo

 de Execução

A seguir, estão os resultados de tempo de execução para os dois algoritmos em diferentes tamanhos de entrada:

| Tamanho de Entrada | Algoritmo Genético | Programação Dinâmica |
|--------------------|--------------------|----------------------|
| 100                | 0.008033 segundos  | 0.000967 segundos    |
| 200                | 0.014998 segundos  | 0.002052 segundos    |
| 400                | 0.030998 segundos  | 0.003025 segundos    |
| 800                | 0.062001 segundos  | 0.009970 segundos    |
| 1600               | 0.122958 segundos  | 0.017997 segundos    |
| 5000               | 0.403004 segundos  | 0.048000 segundos    |
| 20000              | 1.576172 segundos  | 0.189000 segundos    |
| 100000             | 7.908361 segundos  | 0.964000 segundos    |

## Análise Comparativa

Com base nos resultados de tempo de execução, podemos observar que a programação dinâmica é significativamente mais rápida do que o algoritmo genético para resolver o problema da mochila. Em todos os tamanhos de entrada testados, o algoritmo de programação dinâmica apresentou tempos de execução substancialmente menores em comparação com o algoritmo genético.

Embora o algoritmo genético seja conhecido por sua capacidade de encontrar soluções aproximadas, ele é mais adequado para problemas de otimização combinatória de grande escala ou com restrições complexas. No caso do problema da mochila, onde o objetivo é encontrar a solução ótima, a programação dinâmica é uma escolha mais eficiente em termos de tempo.

É importante destacar que o desempenho dos algoritmos pode variar dependendo das características específicas do problema e dos parâmetros escolhidos para cada algoritmo. Portanto, é recomendado realizar análises adicionais e considerar outras métricas de desempenho, além do tempo de execução, ao selecionar o algoritmo mais adequado para resolver o problema da mochila em diferentes cenários.

## Conclusão

Com base na análise realizada, podemos concluir que, para o problema da mochila, o algoritmo de programação dinâmica é mais eficiente em termos de tempo de execução em comparação com o algoritmo genético. Portanto, para situações em que a busca pela solução ótima é prioritária e o tamanho da entrada permite a aplicação da programação dinâmica, essa abordagem é a mais recomendada.

No entanto, é importante considerar que cada algoritmo possui suas próprias vantagens e desvantagens, e a escolha entre eles deve levar em conta as características específicas do problema, os requisitos do projeto e as restrições de recursos disponíveis.
