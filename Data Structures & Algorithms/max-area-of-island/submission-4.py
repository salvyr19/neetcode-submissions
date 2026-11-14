class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if grid == [[0]*len(grid)]*len(grid[0]) :
            return 0
        neighbor = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        row, col = len(grid), len(grid[0])
        color =  2

        def fill(i, j) :
            n = 0
            if not (0<=i<row and 0<=j<col) or grid[i][j] != 1 :
                return 0
            grid[i][j] =  color
            for dr, dc in neighbor : 
                n += fill(i+dr, j+dc)
             
            return 1 + n 

        max_area = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1 :
                    max_area = max(fill(i, j), max_area)
        return max_area
             
