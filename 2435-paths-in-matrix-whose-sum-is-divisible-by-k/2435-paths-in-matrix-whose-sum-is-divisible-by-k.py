class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        MOD = 10**9 + 7
        
        cache = [[[-1 for _ in range(k)] for _ in range(cols)] for _ in range(rows)]
        
        def dfs(r, c, remain):
            if r >= rows or c >= cols:
                return 0
            remain = remain % k
            if cache[r][c][remain] != -1:
                return cache[r][c][remain]
            if r == rows-1 and c == cols-1:
                return 1 if remain == 0 else 0
            
            down = dfs(r+1, c, (remain + grid[r+1][c]) % k if r+1 < rows else remain)
            right = dfs(r, c+1, (remain + grid[r][c+1]) % k if c+1 < cols else remain)
            
            cache[r][c][remain] = (down + right) % MOD
            return cache[r][c][remain]
        
        return dfs(0, 0, grid[0][0] % k)

        # rows=len(grid)
        # cols=len(grid[0])
        # res=0
        # MOD = 10**9 + 7
        # @cache
        # def dfs(r,c,remain):
        #     if r >= rows or c >= cols:  # out of bounds
        #         return 0
        #     remain=(remain + grid[r][c]) % k
        #     if r == rows - 1 and c == cols - 1:  # bottom-right
        #         return 1 if remain == 0 else 0
        #     return (dfs(r+1, c, remain) + dfs(r, c+1, remain)) % MOD


        # return dfs(0,0,0)
        ##OPTIMISED SPACE DP
# class Solution:
#     def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
#         rows, cols = len(grid), len(grid[0])
#         MOD = 10**9 + 7

#         # dp[c][remain] = number of paths to this cell with sum % k == remain
#         dp = [[0] * k for _ in range(cols)]
#         dp[0][grid[0][0] % k] = 1

#         for r in range(rows):
#             new_dp = [[0] * k for _ in range(cols)]
#             for c in range(cols):
#                 for remain in range(k):
#                     val = dp[c][remain]
#                     if val == 0:
#                         continue
#                     # move down
#                     if r + 1 < rows:
#                         new_rem = (remain + grid[r+1][c]) % k
#                         new_dp[c][new_rem] = (new_dp[c][new_rem] + val) % MOD
#                     # move right
#                     if c + 1 < cols:
#                         new_rem = (remain + grid[r][c+1]) % k
#                         new_dp[c+1][new_rem] = (new_dp[c+1][new_rem] + val) % MOD
#             dp = new_dp

#         return dp[cols-1][0]


      
        