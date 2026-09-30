"""
 
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        def bfs(i, j, count):
            q = deque([(i, j)])
            while q:
                x, y = q.popleft()
                if grid[x][y] == 1:
                    count += 1
                    grid[x][y] = 0
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                            q.append((nx,ny))
            return count
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res, bfs(i,j,0))
        return res
