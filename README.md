# 8-Puzzle — Busca em Espaço de Estados

Execute com Python 3.10 ou superior, sem dependências externas.

```sh
python main.py
```

As ações movem o espaço vazio. `U` sobe, `D` desce, `L` vai à esquerda e `R` vai à direita. Cada movimento custa 1.

## Implementação

### `puzzle/state.py`
- `neighbors()` — gera os estados filhos a partir do espaço vazio
- `path()` — reconstrói a sequência de estados do inicial até este
- `actions()` — retorna a sequência de ações usando `path()`

### `algorithms/bfs.py`
- `BFS.search(initial)` - busca em largura com fila

### `algorithms/dfs.py`
- `DFS.search(initial)` - busca em profundidade com pilha e limite padrão de 50 movimentos

### `algorithms/a_star.py`
- `AStar.heuristic(state)` - soma das distâncias de Manhattan das peças numeradas até suas posições no objetivo
- `AStar.search(initial)` - busca A* com fila de prioridade ordenada por custo acumulado mais heurística

## Estrutura

```
├── puzzle/
│   ├── state.py
│   ├── result.py
│   └── base_search.py
├── algorithms/
│   ├── bfs.py
│   ├── dfs.py
│   └── a_star.py
└── main.py
```

