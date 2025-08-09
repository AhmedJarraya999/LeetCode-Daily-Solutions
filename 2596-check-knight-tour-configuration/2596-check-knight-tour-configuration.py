class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n=len(grid)
        directions=[(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
        if grid[0][0]!=0:
                return False
        
        def dfs(step,x,y):
            if step==n*n-1:
                return True
            next_step=step+1
            for dx,dy in directions:
                nx=dx+x
                ny=dy+y
                if 0<=nx<n and 0<=ny<n and grid[nx][ny]==next_step:
                    if dfs(next_step,nx,ny):
                        return True
            return False
        return dfs(0,0,0)

        