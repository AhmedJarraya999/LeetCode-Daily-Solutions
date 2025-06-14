class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        total_steps =0
        start_x,start_y=0,0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]!=-1:
                    total_steps +=1
                if grid[i][j]==1:
                    start_x,start_y=i,j
        def dfs(x,y,steps):
            if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] == -1:
                return 0
            if grid[x][y] == 2:
                return 1 if steps == total_steps else 0
            temp = grid[x][y]
            grid[x][y] = -1
            paths = 0
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                paths += dfs(x + dx, y + dy, steps + 1)
            grid[x][y] = temp
            return paths
        return dfs(start_x, start_y, 1)

        