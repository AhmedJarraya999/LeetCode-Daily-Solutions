class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        directions=[(-1,0),(1,0),(0,1),(0,-1)]
        start_color=grid[row][col]
        n=len(grid)
        m=len(grid[0])
        visited=set()
        boarders=[]
        def dfs(r,c):
            visited.add((r,c))
            is_boarder=False
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if not (0<=nr<n and 0<=nc<m):
                    is_boarder=True
                elif grid[nr][nc]!=start_color:
                    is_boarder=True
                elif (nr,nc) not in visited:
                    dfs(nr,nc)
            if is_boarder:
                boarders.append((r, c))
        dfs(row,col)
        for r,c in boarders:    
            grid[r][c]=color
        return grid