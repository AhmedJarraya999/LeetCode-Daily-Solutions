class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visit=set()
        def dfs(r,c):
            if (r<0 or r==rows or c<0 or c==cols or grid[r][c]==0 or (r,c) in visit):
                return 0
            visit.add((r,c))
            area = 1  
            directions=[[-1,0],[1,0],[0,1],[0,-1]]
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                area += dfs(nr, nc)
            return area


            
        maxarea=0    
        for r in range(rows):
            for c in range(cols):
                maxarea=max(maxarea,dfs(r,c))
        return maxarea

        