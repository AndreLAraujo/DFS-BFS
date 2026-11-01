# Algoritmos de Busca em Grafos: DFS vs BFS em Python

Este repositório contém as implementações em Python dos algoritmos fundamentais de busca em grafos: Busca em Profundidade (DFS) e Busca em Largura (BFS).

## Contextos de Aplicação no Mundo Real

A lógica estrutural exata implementada nestes scripts (a fila com `deque` na BFS e a recursão com pilha de chamadas na DFS) é a base utilizada em sistemas de produção. A diferença no mundo real é que o grafo é construído dinamicamente (ex: consultas a bancos de dados ou APIs) em vez de ser estático.

### 1. BFS (Busca em Largura)
*   **Mecanismo:** Exploração em camadas radiais. Varre toda a vizinhança de um nível (distância 1) antes de avançar para o próximo. Utiliza uma **Fila (Queue - FIFO)**.
*   **Aplicações na Prática (Fila com `deque`):**
    *   **Mapeamento de Redes (Network Discovery):** Em ferramentas de auditoria e segurança, o BFS varre primeiro todos os IPs conectados diretamente a um roteador de origem (nível 1). Só depois de esgotar o nível 1, avança para os dispositivos nos switches vizinhos (nível 2), garantindo o mapeamento da rede local antes da expansão externa.
    *   **Redes Sociais (Graus de Separação):** Para o recurso "Pessoas que talvez conheças", o sistema enfileira as ligações diretas e depois as ligações dessas ligações. A remoção com `popleft()` em O(1) torna a procura pelo caminho mais curto extremamente rápida e eficiente.

### 2. DFS (Busca em Profundidade)
*   **Mecanismo:** Exploração em mergulho vertical. Avança por um ramo até ao seu limite máximo antes de recuar (*backtracking*) para considerar rotas alternativas. Utiliza uma **Pilha (Stack - LIFO)**, através da recursão.
*   **Aplicações na Prática (Pilha e Recursão):**
    *   **Web Crawlers e Brute-Forcing de Diretórios:** Ao mapear a superfície de ataque web, um crawler entra na raiz, acede a `/admin`, entra em `config.php` (nó folha). Quando não há novos links, sofre *backtracking* natural na pilha de execução e testa a próxima pasta do nível anterior (como `/images`).
    *   **Gestores de Pacotes (APT no Linux):** Para instalar um software, a DFS desce a árvore de dependências até à biblioteca de mais baixo nível. Instala-a e vai recuando, instalando as camadas superiores até concluir o pacote principal.

## Arquitetura da Implementação

A representação do grafo foi feita através de uma **Lista de Adjacência** (utilizando dicionários em Python).
*   **Vantagem Técnica:** Permite acesso em tempo constante O(1) aos vizinhos de qualquer vértice. Otimiza o consumo de memória frente às pesadas matrizes de adjacência. Ideal para grafos esparsos.

## Execução e Complexidade

*   **Complexidade de Tempo:** Universal para ambos os algoritmos: **O(V + E)** (onde V = Vértices, E = Arestas). O tempo cresce linearmente conforme a quantidade de nós e conexões do grafo.
*   **Complexidade de Espaço:** **O(V)**. 
    *   Na BFS, a fila armazena no máximo todos os vértices de uma camada específica do grafo.
    *   Na DFS, a pilha de execução armazena o estado correspondente à profundidade do ramo explorado.

## Entendendo o Código do Repositório

O script Python disponibilizado neste repositório implementa os dois algoritmos e testa-os contra um grafo de exemplo não-direcionado composto por 6 vértices (A até F). 

### Dinâmica de Execução:
1. **Topologia do Grafo:** A raiz `A` conecta-se aos vizinhos `B` e `C`. O nó `B` desce para `D` (um nó folha sem saída) e `E`. O nó `C` desce para `F`.
2. **Comportamento da BFS:** Ao iniciar em `A`, a fila (usando `collections.deque`) força a leitura em camadas. O console imprimirá a ordem de visitação `['A', 'B', 'C', 'D', 'E', 'F']`, provando que o nível 1 (`B` e `C`) foi totalmente esgotado antes do algoritmo visitar o nível 2.
3. **Comportamento da DFS:** Ao iniciar em `A`, a função recursiva e a pilha de chamadas (*call stack*) forçam o mergulho. O console imprimirá `['A', 'B', 'D', 'E', 'C', 'F']`. O algoritmo desce de `A` para `B`, mergulha até `D`, sofre um *backtracking* porque `D` não tem vizinhos novos, explora `E`, e só então retorna ao topo para explorar `C` e `F`.

*Nota para Produção:* Este script está otimizado para fins didáticos (retorna a ordem completa de visitação). Num cenário real de roteamento ou segurança, seria inserida uma condicional de paragem imediata (ex: `if atual == alvo:`) assim que o nó desejado fosse encontrado, poupando recursos de processamento.

## Validação de Resultados (Oráculo de Teste)

Para garantir a corretude matemática da implementação da BFS em encontrar o menor caminho, este repositório inclui um script de validação isolado na pasta `validacao/` utilizando o **Algoritmo de Dijkstra**.

*   **Motivo da Escolha:** Enquanto a BFS encontra o menor caminho por quantidade de saltos (níveis) em grafos não-ponderados, o algoritmo de Dijkstra encontra o caminho de custo mínimo em grafos ponderados. Ao tratarmos cada aresta do nosso grafo com peso igual a 1, o resultado de Dijkstra deve ser rigorosamente idêntico ao número de saltos da BFS.
*   **Conclusão:** O uso de Dijkstra serve como um **Oráculo de Teste** (Baseline/Ground Truth). A execução deste script confirma matematicamente que a fila FIFO da BFS explorou a topologia de forma correta e ótima, atestando a confiabilidade do código principal.
