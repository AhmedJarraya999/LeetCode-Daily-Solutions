class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort(reverse=True)
        n=len(grid)
        m=len(grid[0])
        score=0
        for j in range(m):
            max_val = 0
            for i in range(n):
                max_val = max(max_val,grid[i][j])
            score+=max_val
        return score
        