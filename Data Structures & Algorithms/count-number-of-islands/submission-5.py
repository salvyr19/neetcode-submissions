class Solution:
    from collections import deque
    def numIslands(self, grid: List[List[str]]) -> int:
       
        row, col = len(grid), len(grid[0])
        neighbor = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        n_count = 0
        mark = '2'

        def fill(sr, sc) :
            if not (0 <= sr < row and 0 <= sc < col) or grid[sr][sc] != '1' :
                return 
            grid[sr][sc] = mark
            for dr, dc in neighbor :
                fill(sr + dr, sc + dc)
        
        for r in range(0, row) :
            for c in range(0, col) :
                if grid[r][c] == '1':
                    n_count += 1
                    fill(r, c)
        return n_count
               

