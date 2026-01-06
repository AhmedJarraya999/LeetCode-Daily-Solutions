class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n=len(grid)
        for i in range(n):
            defeated=False
            for j in range(n):
                if i!=j and grid[i][j]==0:
                    defeated=True
            if not defeated:
                return i 

        