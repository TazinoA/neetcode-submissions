"""
have a count, dfs on 1s
for each 1, look at the blocks around, if the block is 0, or out of bounds add 1
to perimiter
"""
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = set()
        perimeter = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(x, y):
            nonlocal perimeter
            if grid[x][y] == 0 or (x, y) in visited:
                    return
                
            visited.add((x, y))
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if nx < 0 or nx >= ROWS or ny < 0 or ny >= COLS or grid[nx][ny] == 0:
                    perimeter += 1
                if 0 <= nx < ROWS and 0 <= ny < COLS and (nx, ny) not in visited:
                    dfs(nx, ny)
         
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return perimeter
        #return perimeter
        
            
