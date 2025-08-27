class Solution(object):
    def lenOfVDiagonal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def memoization(i, j, x, d, k):
            if not (0 <= i < n and 0 <= j < m):
                return 0
            if grid[i][j] != x:
                return 0
            if lookup[k][x][d][i][j] == 0:
                ni, nj = i + directions[d][0], j + directions[d][1]
                nx = 0 if x == 2 else 2
                result = memoization(ni, nj, nx, d, k) + 1
                if k != 1:
                    nd = (d + 1) % 4
                    result = max(result, memoization(ni, nj, nx, nd, k + 1) + 1)
                lookup[k][x][d][i][j] = result
            return lookup[k][x][d][i][j]

        n, m = len(grid), len(grid[0])
        directions = ((1, 1), (1, -1), (-1, -1), (-1, 1))
        lookup = [[[[[0] * m for _ in range(n)] for _ in range(4)] for _ in range(3)] for _ in range(2)]
        result = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    for d in range(4):
                        result = max(result, memoization(i, j, 1, d, 0))

        return result

# from functools import lru_cache
# from typing import List

# class Solution:
#     def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
#         n=len(grid)
#         m=len(grid[0])
        
#         # directions in proper clockwise order: DR → DL → UL → UR
#         dirs = [(1,1), (1,-1), (-1,-1), (-1,1)]
        
#         def nextClockwise(d):
#             return (d + 1) % 4
        
#         def in_bounds(r: int, c: int) -> bool:
#             return 0 <= r < n and 0 <= c < m
        
#         def expectedValue(step):
#             if step==0:
#                 return 1
#             return 2 if step%2==1 else 0
        
#         @lru_cache(None)
#         def dfs(r,c,dirIdx,step,turn):
#             if not in_bounds(r, c): return 0
#             if grid[r][c] != expectedValue(step): return 0
            
#             res=1
#             #dfs dp call
#             # Move forward
#             dr, dc = dirs[dirIdx]
#             res = max(res, 1 + dfs(r+dr, c+dc, dirIdx, step+1, turn))

#             #call recursive after making 90degree turn
#             if turn ==0:
#                 newdir = nextClockwise(dirIdx)
#                 dr,dc = dirs[newdir]
#                 res = max(res, 1 + dfs(r+dr, c+dc, newdir, step+1, 1))  
#             return res
        
#         ans = 0
#         for r in range(n):
#             for c in range(m):
#                 if grid[r][c]==1:
#                     for d in range(4):
#                         ans=max(ans,dfs(r,c,d,0,0))
#         return ans
