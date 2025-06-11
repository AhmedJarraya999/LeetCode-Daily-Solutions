class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        res=0
        rows=len(grid)
        cols=len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    row_com= any(grid[r][x]==1 for x in range(cols) if x!=c)
                    col_com=any(grid[x][c]==1 for x in range(rows) if x!=r)
                    if row_com or col_com:
                        res+=1
        return res

        