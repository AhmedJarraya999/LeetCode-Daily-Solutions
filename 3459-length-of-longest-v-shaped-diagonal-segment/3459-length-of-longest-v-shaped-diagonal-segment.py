from typing import List
from functools import cache

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dirs = [(-1, -1), (-1, 1), (1, 1), (1, -1)]  # TL, TR, BR, BL

        def expected_value(idx: int) -> int:
            if idx == 0:
                return 1
            return 2 if idx % 2 == 1 else 0

        @cache
        def dfs(i: int, j: int, idx: int, turned: bool, d: int) -> int:
            # bounds + value check for the current position in the sequence
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != expected_value(idx):
                return 0

            next_idx = idx + 1
            di, dj = dirs[d]

            # Option 1: continue straight in the same direction
            best = 1 + dfs(i + di, j + dj, next_idx, turned, d)

            # Option 2: (if not yet turned) turn clockwise once and then keep that new dir
            if not turned:
                new_d = (d + 1) % 4
                ndi, ndj = dirs[new_d]
                best = max(best, 1 + dfs(i + ndi, j + ndj, next_idx, True, new_d))

            return best

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:  # must start with 1
                    for d in range(4):
                        ans = max(ans, dfs(i, j, 0, False, d))
        return ans

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
