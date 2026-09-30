"""
 
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(i, j, count):
            if grid[i][j] == 0:
                return count
            count += 1
            grid[i][j] = 0
            for dx, dy in directions:
                nx, ny = i + dx, j + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    count = dfs(nx, ny, count)
            return count

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    num = dfs(i, j, 0)
                    res = max(res, num)
        return res
