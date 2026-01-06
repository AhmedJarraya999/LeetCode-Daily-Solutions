class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            defeated=False
            for j in range(len(grid)):
                if i!=j and grid[i][j]==0:
                    defeated=True
            if not defeated:
                return i 

        