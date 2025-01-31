from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Apenas 4 direções (sem diagonais)
        island_size = {}
        island_id = 2  # Começar a numerar ilhas a partir de 2 para evitar confusão com 0s e 1s

        def dfs(x, y, island_id):
            """Marca a ilha e calcula seu tamanho."""
            stack = [(x, y)]
            grid[x][y] = island_id
            size = 0

            while stack:
                i, j = stack.pop()
                size += 1
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                        grid[ni][nj] = island_id
                        stack.append((ni, nj))
            return size

        # Passo 1: Marcar ilhas existentes e calcular seus tamanhos
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island_size[island_id] = dfs(i, j, island_id)
                    island_id += 1

        print(island_size)

        # Se não há zeros, a maior ilha já é o grid inteiro
        if not island_size:
            return n * n

        max_island = max(island_size.values(), default=0)  # Caso inicial: maior ilha já existente

        # Passo 2: Tentar transformar um 0 em 1 e calcular o novo tamanho da ilha
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen_islands = set()
                    new_size = 1  # Conta o próprio 0 virando 1
                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                            island_id = grid[ni][nj]
                            if island_id not in seen_islands:
                                seen_islands.add(island_id)
                                new_size += island_size[island_id]
                    max_island = max(max_island, new_size)

        return max_island