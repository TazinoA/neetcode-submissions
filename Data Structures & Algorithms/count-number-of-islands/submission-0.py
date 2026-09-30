
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def dfs(i, j):
            if grid[i][j] == "0":
                return
            
            grid[i][j] = "0"
            for dx, dy in directions:
                nx, ny = i+dx, j+dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    dfs(nx, ny)
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        return res
            