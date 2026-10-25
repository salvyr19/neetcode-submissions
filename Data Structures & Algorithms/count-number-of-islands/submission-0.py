class Solution:
    from collections import deque
    def numIslands(self, grid: List[List[str]]) -> int:
       
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        # les 4 déplacements possibles : bas, haut, droite, gauche
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(rows):
            for c in range(cols):
                # une case de terre jamais visitée : c'est une nouvelle île
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    q = deque([(r, c)])
                    visited.add((r, c))

                    # j'explore toute cette île
                    while q:
                        # je sors la prochaine case à examiner
                        row, col = q.popleft()
                        for dr, dc in directions:
                            nr, nc = row + dr, col + dc
                            # je garde le voisin s'il est dans la grille, de terre et pas encore vu
                            if (0 <= nr < rows and 0 <= nc < cols
                                    and grid[nr][nc] == "1"
                                    and (nr, nc) not in visited):
                                visited.add((nr, nc))
                                q.append((nr, nc))
        return islands