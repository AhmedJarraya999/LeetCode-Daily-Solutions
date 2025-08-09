class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        n=len(grid)
        m=len(grid[0])
        count=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    for dr,dc in directions:
                        nr=dr+i
                        nc=dc+j
                        if nr < 0 or nr >= n or nc < 0 or nc >= m or grid[nr][nc] == 0:
                            count += 1
        return count





        
        